import unittest

from pulp_glance.common import models


class TestBasics(unittest.TestCase):
    def test_init_info(self):
        image = models.GlanceImage('abc', 'xyz')

        self.assertEqual(image.image_id, 'abc')

    def test_unit_key(self):
        image = models.GlanceImage('abc', 'xyz')

        self.assertEqual(image.unit_key, {'image_id': 'abc'})

    def test_relative_path(self):
        image = models.GlanceImage('abc', 'xyz')

        self.assertEqual(image.relative_path, 'glance_image/abc')

    def test_metadata(self):
        image = models.GlanceImage('abc', 'xyz')
        metadata = image.unit_metadata
        self.assertTrue(False)

