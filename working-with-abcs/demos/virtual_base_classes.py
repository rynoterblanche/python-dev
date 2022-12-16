import unittest
from collections.abc import Sized, Iterable, Iterator


class MyCustomSized:
    def __len__(self):
        return 10


class MyCustomIterator:
    def __iter__(self):
        return self

    def __next__(self):
        return "next"


class TestIsInstance(unittest.TestCase):
    """
    Abstract base classes can extend 'issubclass' and 'isinstance' mechanisms to enable structural (or duck) type
    checks with subclasses. Virtual base classes like the ones from collections.abc can test for the implementation of
    protocols in your custom subclasses, as shown in these tests.
    """

    def test_MyCustomSized_is_instance_of_Sized(self):
        self.assertIsInstance(MyCustomSized(), Sized)

    def test_MyCustomIterator_is_instance_of_Iterable(self):
        self.assertIsInstance(MyCustomIterator(), Iterable)

    def test_MyCustomIterator_is_instance_of_Iterator(self):
        self.assertIsInstance(MyCustomIterator(), Iterator)
