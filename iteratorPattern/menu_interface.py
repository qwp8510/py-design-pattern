from abc import ABC, abstractmethod


class MenuInterface(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
