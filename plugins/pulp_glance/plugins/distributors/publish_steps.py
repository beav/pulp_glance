from gettext import gettext as _
# NEED TO VERIFY
import logging
import os

from pulp.plugins.util.publish_step import PublishStep, UnitPublishStep, \
    AtomicDirectoryPublishStep, SaveTarFilePublishStep

from pulp_glance.common import constants
from pulp_glance.plugins.distributors import configuration


_LOG = logging.getLogger(__name__)


class WebPublisher(PublishStep):
    """
    Glance Image Web publisher class that is responsible for the actual publishing
    of a glance image repository via a web server
    """

    def __init__(self, repo, publish_conduit, config):
        """
        :param repo: Pulp managed Yum repository
        :type  repo: pulp.plugins.model.Repository
        :param publish_conduit: Conduit providing access to relative Pulp functionality
        :type  publish_conduit: pulp.plugins.conduits.repo_publish.RepoPublishConduit
        :param config: Pulp configuration for the distributor
        :type  config: pulp.plugins.config.PluginCallConfiguration
        """
        super(WebPublisher, self).__init__(constants.PUBLISH_STEP_WEB_PUBLISHER,
                                           repo, publish_conduit, config)

        publish_dir = configuration.get_web_publish_dir(repo, config)
        app_file = configuration.get_redirect_file_name(repo)
        app_publish_location = os.path.join(configuration.get_app_publish_dir(config), app_file)
        self.web_working_dir = os.path.join(self.get_working_dir(), 'web')
        master_publish_dir = configuration.get_master_publish_dir(repo, config)
        atomic_publish_step = AtomicDirectoryPublishStep(self.get_working_dir(),
                                                         [('web', publish_dir),
                                                          (app_file, app_publish_location)],
                                                         master_publish_dir,
                                                         step_type=constants.PUBLISH_STEP_OVER_HTTP)
        atomic_publish_step.description = _('Making files available via web.')
        self.add_child(PublishImagesStep())
        self.add_child(atomic_publish_step)


class PublishImagesStep(UnitPublishStep):
    """
    Publish Images
    """

    def __init__(self):
        super(PublishImagesStep, self).__init__(constants.PUBLISH_STEP_IMAGES,
                                                constants.IMAGE_TYPE_ID)
        self.context = None
        self.redirect_context = None
        self.description = _('Publishing Image Files.')

    def initialize(self):
        """
        Initialize the metadata contexts
        """
        self.redirect_context = RedirectFileContext(self.get_working_dir(),
                                                    self.get_conduit(),
                                                    self.parent.config,
                                                    self.get_repo())
        self.redirect_context.initialize()

    def process_unit(self, unit):
        """
        Link the unit to the image content directory and the package_dir

        :param unit: The unit to process
        :type unit: pulp_glance.common.models.GlanceImage
        """
        self.redirect_context.add_unit_metadata(unit)
        target_base = os.path.join(self.get_web_directory(), unit.unit_key['image_id'])
        # TODO: fix
        #for file_name in files:
        #    self._create_symlink(os.path.join(unit.storage_path, file_name),
        #                         os.path.join(target_base, file_name))

    def finalize(self):
        """
        Close & finalize each the metadata context
        """
        if self.redirect_context:
            self.redirect_context.finalize()

    def get_web_directory(self):
        """
        Get the directory where the files published to the web have been linked
        """
        return os.path.join(self.get_working_dir(), 'web')
