import unittest

from pulp_glance.common import models


class TestBasics(unittest.TestCase):
    def test_init_info(self):
        image = models.GlanceImage('70924d6fa4b2d745185fa4660703a5c0')

        self.assertEqual(image.image_checksum, '70924d6fa4b2d745185fa4660703a5c0')

    def test_unit_key(self):
        image = models.GlanceImage('70924d6fa4b2d745185fa4660703a5c0')

        self.assertEqual(image.unit_key, {'image_checksum': '70924d6fa4b2d745185fa4660703a5c0'})

    def test_relative_path(self):
        image = models.GlanceImage('70924d6fa4b2d745185fa4660703a5c0')

        self.assertEqual(image.relative_path, 'glance_image/70924d6fa4b2d745185fa4660703a5c0')

    def test_metadata(self):
        image = models.GlanceImage('70924d6fa4b2d745185fa4660703a5c0')
        metadata = image.unit_metadata
        self.assertEqual(metadata, {})
