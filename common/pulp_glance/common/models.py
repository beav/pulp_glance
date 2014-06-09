import os

from pulp_glance.common import constants


class GlanceImage(object):
    TYPE_ID = constants.IMAGE_TYPE_ID

    def __init__(self, image_id, arch):
        """
        :param image_id:    image UUID
        :type  image_id:    basestring
        :param arch:        image architecture
        :type  arch:        basestring
        """
        self.image_id = image_id
        self.arch = arch

    @property
    def unit_key(self):
        """
        :return:    unit key
        :rtype:     dict
        """
        return {
            'image_id': self.image_id
        }

    @property
    def relative_path(self):
        """
        :return:    the relative path to where this image's directory should live
        :rtype:     basestring
        """
        return os.path.join(self.TYPE_ID, self.image_id)

    @property
    def unit_metadata(self):
        """
        :return:    a subset of the complete glance metadata about this image,
                    including only what pulp_glance cares about
        :rtype:     dict
        """
        return {
            'arch': self.arch,
        }
