import unittest
# NEED TO VERIFY

from mock import Mock
from pulp.common.constants import REPO_NOTE_TYPE_KEY

from pulp_glance.common import constants
from pulp_glance.extensions.admin import cudl


class TestCreateGlanceRepositoryCommand(unittest.TestCase):
    def test_default_notes(self):
        # make sure this value is set and is correct
        self.assertEqual(cudl.CreateGlanceRepositoryCommand.default_notes.get(REPO_NOTE_TYPE_KEY),
                         constants.REPO_NOTE_GLANCE)

    def test_importer_id(self):
        # this value is required to be set, so just make sure it's correct
        self.assertEqual(cudl.CreateGlanceRepositoryCommand.IMPORTER_TYPE_ID,
                         constants.IMPORTER_TYPE_ID)

    def test_describe_distributors_override_auto_publish(self):
        command = cudl.CreateGlanceRepositoryCommand(Mock())
        user_input = {
            'auto-publish': False
        }
        result = command._describe_distributors(user_input)
        self.assertEquals(result[0]["auto_publish"], False)
