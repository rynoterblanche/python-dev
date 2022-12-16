import unittest
from collections.abc import Hashable


class TestNonTransitiveSubclasses(unittest.TestCase):
    def test_object_issubclass_of_hashable(self):
        # object.__hash__ is not None
        self.assertIsNotNone(object.__hash__)
        self.assertTrue(issubclass(object, Hashable))

    def test_list_issubclass_of_object(self):
        self.assertTrue(issubclass(list, object))

    def test_list_issubclass_of_hashable(self):
        # list.__hash__ is None
        self.assertIsNone(list.__hash__)
        self.assertFalse(issubclass(list, Hashable))
