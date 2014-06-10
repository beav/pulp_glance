import unittest
# NEED TO VERIFY

from mock import Mock
from pulp.common.constants import REPO_NOTE_TYPE_KEY
from pulp.devel.unit.util import compare_dict

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


class TestUpdateGlanceRepositoryCommand(unittest.TestCase):

    def setUp(self):
        self.context = Mock()
        self.context.config = {'output': {'poll_frequency_in_seconds': 3}}
        self.command = cudl.UpdateGlanceRepositoryCommand(self.context)
        self.command.poll = Mock()
        self.mock_repo_response = Mock(response_body={})
        self.context.server.repo.repository.return_value = self.mock_repo_response
        self.unit_search_command = Mock(response_body=[{u'metadata': {u'image_id': 'bar'}}])
        self.context.server.repo_unit.search.return_value = self.unit_search_command

    def test_image_not_found(self):
       # TODO: fix
       pass

    def test_repo_update_distributors(self):
       # TODO: fix
       pass
