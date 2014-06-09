import unittest
# NEED TO VERIFY

import mock
from pulp.plugins.config import PluginCallConfiguration
from pulp.plugins.importer import Importer
from pulp.plugins.model import Repository

import data
from pulp_glance.common import constants
from pulp_glance.common.models import GlanceImage
from pulp_glance.plugins.importers.importer import GlanceImageImporter, entry_point
from pulp_glance.plugins.importers import upload


class TestEntryPoint(unittest.TestCase):
    def test_returns_importer(self):
        importer, config = entry_point()

        self.assertTrue(issubclass(importer, Importer))

    def test_returns_config(self):
        importer, config = entry_point()

        # make sure it's at least the correct type
        self.assertTrue(isinstance(config, dict))


class TestBasics(unittest.TestCase):
    def test_metadata(self):
        metadata = GlanceImageImporter.metadata()

        self.assertEqual(metadata['id'], constants.IMPORTER_TYPE_ID)
        self.assertEqual(metadata['types'], [constants.IMAGE_TYPE_ID])
        self.assertTrue(len(metadata['display_name']) > 0)


class TestUploadUnit(unittest.TestCase):
    def setUp(self):
        self.unit_key = {'arch': data.cirros_img_metadata['arch']}
        self.repo = Repository('repo1')
        self.conduit = mock.MagicMock()
        self.config = PluginCallConfiguration({}, {})

    @mock.patch('pulp_glance.plugins.importers.upload.save_models', spec_set=True)
    def test_save_conduit(self, mock_save):
        GlanceImageImporter().upload_unit(self.repo, constants.IMAGE_TYPE_ID, self.unit_key,
                                     {}, data.cirros_img_path, self.conduit, self.config)

        self.assertTrue(False)
        conduit = mock_save.call_args[0][0]

        self.assertTrue(conduit is self.conduit)

    @mock.patch('pulp_glance.plugins.importers.upload.save_models', spec_set=True)
    def test_saved_models(self, mock_save):
        GlanceImageImporter().upload_unit(self.repo, constants.IMAGE_TYPE_ID, self.unit_key,
                                     {}, data.cirros_img_path, self.conduit, self.config)

        self.assertTrue(False)
        models = mock_save.call_args[0][1]

        for model in models:
            self.assertTrue(isinstance(model, GlanceImage))

        ids = [m.image_id for m in models]

        self.assertEqual(tuple(ids), data.busybox_ids)

    @mock.patch('pulp_glance.plugins.importers.upload.save_models', spec_set=True)
    def test_saved_filepath(self, mock_save):
        GlanceImageImporter().upload_unit(self.repo, constants.IMAGE_TYPE_ID, self.unit_key,
                                     {}, data.cirros_img_path, self.conduit, self.config)

        self.assertTrue(False)
        path = mock_save.call_args[0][3]

        self.assertEqual(path, data.cirros_img_path)


class TestImportUnits(unittest.TestCase):

    def setUp(self):
        self.unit_key = {'arch': data.cirros_img_metadata['arch']}
        self.source_repo = Repository('repo_source')
        self.dest_repo = Repository('repo_dest')
        self.conduit = mock.MagicMock()
        self.config = PluginCallConfiguration({}, {})

    def test_import_all(self):
        mock_unit = mock.Mock(unit_key={'image_id': 'foo'}, metadata={})
        self.conduit.get_source_units.return_value = [mock_unit]
        result = GlanceImageImporter().import_units(self.source_repo, self.dest_repo, self.conduit,
                                                    self.config)
        self.assertEquals(result, [mock_unit])
        self.conduit.associate_unit.assert_called_once_with(mock_unit)

    def test_import(self):
        mock_unit = mock.Mock(unit_key={'image_id': 'foo'}, metadata={})
        result = GlanceImageImporter().import_units(self.source_repo, self.dest_repo, self.conduit,
                                                    self.config, units=[mock_unit])
        self.assertEquals(result, [mock_unit])
        self.conduit.associate_unit.assert_called_once_with(mock_unit)


class TestValidateConfig(unittest.TestCase):
    def test_always_true(self):
        for repo, config in [['a', 'b'], [1, 2], [mock.Mock(), {}], ['abc', {'a': 2}]]:
            # make sure all attempts are validated
            self.assertEqual(GlanceImageImporter().validate_config(repo, config), (True, ''))


class TestRemoveUnit(unittest.TestCase):

    def setUp(self):
        self.repo = Repository('repo_source')
        self.conduit = mock.MagicMock()
        self.config = PluginCallConfiguration({}, {})
        self.mock_unit = mock.Mock(unit_key={'image_id': 'foo'}, metadata={})

    @mock.patch('pulp_glance.plugins.importers.importer.manager_factory.repo_manager')
    def test_remove(self, mock_repo_manager):
        mock_repo_manager.return_value.get_repo_scratchpad.return_value = \
            {u'tags': {'apple': 'bar'}}
        GlanceImageImporter().remove_units(self.repo, [self.mock_unit], self.config)
        mock_repo_manager.return_value.set_repo_scratchpad.assert_called_once_with(
            self.repo.id, {u'tags': {'apple': 'bar'}}
        )
