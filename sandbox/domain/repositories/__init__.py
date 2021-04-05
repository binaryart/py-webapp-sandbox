from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, model):
        pass

    @abstractmethod
    def remove(self, id):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def find(self):
        pass

