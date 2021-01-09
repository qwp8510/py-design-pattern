from abc import ABC, abstractmethod


class EmailInterface(ABC):
    @abstractmethod
    def register_subject(self, user, model):
        pass

    @abstractmethod
    def remove_subject(self, user):
        pass

    @abstractmethod
    def send(self):
        pass
