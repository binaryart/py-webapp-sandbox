from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, model):
        pass

    @abstractmethod
    def remove(self, guid):
        pass

    @abstractmethod
    def get(self, guid):
        pass

    @abstractmethod
    def find(self):
        pass

