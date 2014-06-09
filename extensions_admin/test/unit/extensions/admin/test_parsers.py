import unittest
# NEED TO VERIFY

from pulp_glance.extensions.admin import parsers


class TestParseColonSeparated(unittest.TestCase):

    def test_with_value(self):
        result = parsers.parse_colon_separated(['foo:bar'])
        self.assertEquals(result, [['foo', 'bar']])

    def test_with_none(self):
        result = parsers.parse_colon_separated(None)
        self.assertEquals(result, [])

    def test_with_no_colon(self):
        self.assertRaises(ValueError, parsers.parse_colon_separated, ['bar'])

    def test_with_no_value_before_colon(self):
        self.assertRaises(ValueError, parsers.parse_colon_separated, [':bar'])

    def test_with_no_value_after_colon(self):
        self.assertRaises(ValueError, parsers.parse_colon_separated, ['foo:'])

    def test_with_multiple_colon(self):
        result = parsers.parse_colon_separated(['foo:bar:baz'])
        self.assertEquals(result, [['foo:bar', 'baz']])
