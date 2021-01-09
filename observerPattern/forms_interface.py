from abc import ABC, abstractmethod


class FormsInterface(ABC):
    @abstractmethod
    def send(self):
        pass
