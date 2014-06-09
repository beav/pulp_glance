import json
# NEED TO VERIFY
import os
import shutil
import tempfile
import unittest

import mock
from pulp.plugins.model import Unit
from pulp.server.managers import factory
from pulp.server.managers.repo.cud import RepoManager

import data
from pulp_glance.common import constants
from pulp_glance.common.models import GlanceImage
from pulp_glance.plugins.importers import upload


factory.initialize()


metadata = {
    'id1': {'parent': 'id2', 'size': 1024},
    'id2': {'parent': 'id3', 'size': 1024},
    'id3': {'parent': 'id4', 'size': 1024},
    'id4': {'parent': None, 'size': 1024},
}


class TestGetModels(unittest.TestCase):
    def test_full_metadata(self):
        models = upload.get_models(metadata, {'image_id': 'id1'})

        self.assertEqual(len(models), len(metadata))
        for m in models:
            self.assertTrue(isinstance(m, GlanceImage))
            self.assertTrue(m.image_id in metadata)

        ids = [m.image_id for m in models]
        self.assertEqual(set(ids), set(metadata.keys()))

    def test_mask(self):
        models = upload.get_models(metadata, {'image_id': 'id1'}, mask_id='id3')

        self.assertEqual(len(models), 2)
        # make sure this only returns the first two and masks the others
        for m in models:
            self.assertTrue(m.image_id in ['id1', 'id2'])


class TestSaveModels(unittest.TestCase):
    def setUp(self):
        self.conduit = mock.MagicMock()

    @mock.patch('os.path.exists', return_value=True, spec_set=True)
    def test_path_exists(self, mock_exists):
        model = GlanceImage('abc123', 'xyz789')

        upload.save_models(self.conduit, [model], (model.image_id,), data.cirros_img_path)

        self.assertEqual(self.conduit.save_unit.call_count, 1)
        self.conduit.init_unit.assert_called_once_with(constants.IMAGE_TYPE_ID, model.unit_key,
                                                       model.unit_metadata, model.relative_path)

        self.conduit.save_unit.assert_called_once_with(self.conduit.init_unit.return_value)

