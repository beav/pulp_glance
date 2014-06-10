import os

from pulp_glance.common import constants


class GlanceImage(object):
    TYPE_ID = constants.IMAGE_TYPE_ID

    def __init__(self, image_checksum):
        # TODO: add image_size
        """
        :param image_checksum:    MD5 sum
        :type  image_checksum:    basestring
        """
        self.image_checksum = image_checksum

    @property
    def unit_key(self):
        """
        :return:    unit key
        :rtype:     dict
        """
        return {
            'image_checksum': self.image_checksum
        }

    @property
    def relative_path(self):
        """
        :return:    the relative path to where this image's directory should live
        :rtype:     basestring
        """
        return os.path.join(self.TYPE_ID, self.image_checksum)

    @property
    def unit_metadata(self):
        """
        :return:    a subset of the complete glance metadata about this image,
                    including only what pulp_glance cares about
        :rtype:     dict
        """
        return {}
