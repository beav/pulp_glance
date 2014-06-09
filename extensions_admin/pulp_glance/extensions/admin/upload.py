import hashlib
# NEED TO VERIFY

from pulp.client.commands.repo.upload import UploadCommand

from pulp_glance.common import constants


class UploadGlanceImageCommand(UploadCommand):
    def determine_type_id(self, filename, **kwargs):
        """
        We only support one content type, so this always returns that.

        :return: ID of the type of file being uploaded
        :rtype:  str
        """
        return constants.IMAGE_TYPE_ID


    def generate_unit_key_and_metadata(self, filename, **kwargs):
        """
        Generates the unit key and metadata.

        :param filename: full path to the file being uploaded
        :type  filename: str, None

        :param kwargs: arguments passed into the upload call by the user
        :type  kwargs: dict

        :return: tuple of unit key and metadata to upload for the file
        :rtype:  tuple
        """
        checksum = self._find_image_md5sum(filename)
        unit_key = {'checksum': checksum}
        metadata = {}

        return unit_key, metadata

   def _find_image_md5sum(self, filename):
        """
        Return an MD5 sum for a given filename. Glance also uses MD5 sums for
        images, which is why we use it here as well.
        """
        md5 = hashlib.md5()
        with open(filename,'rb') as f: 
            for chunk in iter(lambda: f.read(128 * md5.block_size), b''): 
                 md5.update(chunk)
        return md5.hexdigest()
