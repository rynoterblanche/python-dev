from abc import ABC, abstractmethod


class Sink(ABC):

    @staticmethod
    @abstractmethod
    def abstract_static_method():
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        raise NotImplementedError

    @property
    @abstractmethod
    def abstract_property(self):
        raise NotImplementedError

    @abstract_property.setter
    @abstractmethod
    def abstract_property(self, value):
        raise NotImplementedError
