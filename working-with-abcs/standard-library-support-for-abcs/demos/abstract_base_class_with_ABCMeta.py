import unittest
from abc import ABCMeta


class Sink(metaclass=ABCMeta):
    """
    Abstract Base Class

    This base class uses ABCMeta and so must explicitly mention metaclass as well as override the '__subclasshook__'
    in order to define its structure.
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Returns True for definitive subclass matches
        """

        return (
                hasattr(subclass, "write") and callable(subclass.write)
                and
                hasattr(subclass, "load") and callable(subclass.load)
        )

    def flush(self):
        print("Flushing Sink!", type(self).__name__)


class FileSink:
    """Has no explicit inheritance relationship with Sink, however 'Sink.__subclasshook__' creates a subclass
     relationship to Sink"""

    def write(self):
        print("Writing to file!", type(self).__name__)

    def load(self):
        print("loading", type(self).__name__)


class ConsoleSink:
    """Has no explicit inheritance relationship with Sink, however 'Sink.__subclasshook__' creates a subclass
     relationship to Sink"""

    def write(self):
        print("Writing to console!", type(self).__name__)

    def load(self):
        print("loading", type(self).__name__)


class UnrelatedSink:
    """Not a subclass of type Sink"""

    def write_other(self):
        print("Writing to other!", type(self).__name__)


class TestsIsSubClassOfSink(unittest.TestCase):

    def test_console_sink_is_subclass(self):
        self.assertTrue(issubclass(ConsoleSink, Sink))

    def test_file_sink_is_subclass(self):
        self.assertTrue(issubclass(FileSink, Sink))

    def test_unrelated_sink_is_not_subclass(self):
        self.assertFalse(issubclass(UnrelatedSink, Sink))


class TestsIsInstanceOfSink(unittest.TestCase):

    def test_file_sink_is_instance(self):
        self.assertTrue(isinstance(FileSink(), Sink))

    def test_console_sink_is_instance(self):
        self.assertTrue(isinstance(ConsoleSink(), Sink))

    def test_unrelated_sink_is_not_instance(self):
        self.assertFalse(isinstance(UnrelatedSink(), Sink))


class TestFlushMroFromSinkSubClasses(unittest.TestCase):

    def test_console_sink_cannot_flush(self):
        """ ConsoleSink cannot invoke methods on virtual base classes via MRO"""
        cs = ConsoleSink()
        with self.assertRaises(AttributeError):
            cs.flush()

    def test_file_sink_cannot_flush(self):
        """ FileSink cannot invoke methods on virtual base classes via MRO"""
        cs = FileSink()
        with self.assertRaises(AttributeError):
            cs.flush()
