from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def start(self):
        raise NotImplementedError()

