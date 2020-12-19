from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute():
        pass

    @abstractmethod
    def undo():
        pass