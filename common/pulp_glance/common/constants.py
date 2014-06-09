IMAGE_TYPE_ID = 'glance_image'
IMPORTER_TYPE_ID = 'glance_importer'
IMPORTER_CONFIG_FILE_NAME = 'server/plugins.conf.d/glance_importer.json'
DISTRIBUTOR_WEB_TYPE_ID = 'glance_distributor_web'
DISTRIBUTOR_EXPORT_TYPE_ID = 'glance_distributor_export'
CLI_WEB_DISTRIBUTOR_ID = 'glance_web_distributor_name_cli'
CLI_EXPORT_DISTRIBUTOR_ID = 'glance_export_distributor_name_cli'
DISTRIBUTOR_CONFIG_FILE_NAME = 'server/plugins.conf.d/glance_distributor.json'
DISTRIBUTOR_EXPORT_CONFIG_FILE_NAME = 'server/plugins.conf.d/glance_export_distributor.json'

REPO_NOTE_GLANCE = 'glance-repo'

# Config keys for the distributor plugin conf
CONFIG_KEY_GLANCE_PUBLISH_DIRECTORY = 'glance_publish_directory'
CONFIG_VALUE_GLANCE_PUBLISH_DIRECTORY = '/var/lib/pulp/published/glanceimages'
CONFIG_KEY_EXPORT_FILE = 'export_file'

# Config keys for a distributor instance in the database
CONFIG_KEY_REDIRECT_URL = 'redirect-url'
CONFIG_KEY_PROTECTED = 'protected'
CONFIG_KEY_REPO_REGISTRY_ID = 'repo-registry-id'

# Keys that are specified on the repo config
PUBLISH_STEP_WEB_PUBLISHER = 'publish_to_web'
PUBLISH_STEP_EXPORT_PUBLISHER = 'export_to_tar'
PUBLISH_STEP_IMAGES = 'publish_images'
PUBLISH_STEP_OVER_HTTP = 'publish_images_over_http'
PUBLISH_STEP_DIRECTORY = 'publish_directory'
PUBLISH_STEP_TAR = 'save_tar'
