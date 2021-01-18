from abc import ABC, abstractmethod


class MenuInterface(ABC):
    @property
    @abstractmethod
    def item(self):
        pass
