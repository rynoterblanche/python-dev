import unittest
from abc import ABC, abstractmethod


class Sink(ABC):
    """
    Abstract Base Class

    This base class inherits from ABC and so does not reference metaclass at all. This is the preferred approach to
    introduce base classes. It is clearer, more concise and more widely understood than metaclass.

    In addition, ABC introduces other benefits like the @abstractmethod method decorator:

    @abstractmethod helps define the structure of a base class much more intuitively and replaces the need to override
    '__subclasshook__'
    """

    @abstractmethod
    def write(self):
        print("Writing to file!", type(self).__name__)

    @abstractmethod
    def load(self):
        raise NotImplementedError


class FileSink(Sink):
    """Explicitly inherits from Sink, and overrides the required abstract methods"""

    def write(self):
        print("Writing to file!", type(self).__name__)

    def load(self):
        print("loading", type(self).__name__)


class ConsoleSink(Sink):
    """Explicitly inherits from Sink, and overrides the required abstract methods"""

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
