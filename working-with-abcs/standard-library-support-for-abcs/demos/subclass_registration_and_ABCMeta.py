import unittest
from abc import ABCMeta


class Sink(metaclass=ABCMeta):
    """Abstract Base Class"""

    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Returns True for definitive subclass matches, otherwise returns NotImplemented in order to proceed with other
        subclass checks (for example registered subclasses) and via MRO lookup

        NOTE - using subclass registration incorrectly can unknowingly cause issues and weaken the base class concept.
        Registration can bypass interface detection.
        """

        return (
                (
                        hasattr(subclass, "write") and callable(subclass.write)
                        and
                        hasattr(subclass, "load") and callable(subclass.load)
                )
                or
                NotImplemented
        )


class ConsoleSink:
    """Has no explicit inheritance relationship with Sink, however 'Sink.__subclasshook__' creates a subclass
     relationship to Sink"""

    def write(self):
        print("Writing to console!", type(self).__name__)

    def load(self):
        print("loading", type(self).__name__)


@Sink.register
class ApiSink:
    """ApiSink is a registered subclass of Sink"""
    pass


class TestsIsSubClassOfSink(unittest.TestCase):

    def test_console_sink_is_subclass(self):
        self.assertTrue(issubclass(ConsoleSink, Sink))

    def test_api_sink_is_subclass(self):
        self.assertTrue(issubclass(ApiSink, Sink))


class TestsIsInstanceOfSink(unittest.TestCase):

    def test_console_sink_is_instance(self):
        self.assertTrue(isinstance(ConsoleSink(), Sink))

    def test_api_sink_is_instance(self):
        self.assertTrue(isinstance(ConsoleSink(), Sink))
