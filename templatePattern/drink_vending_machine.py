from abc import ABC, abstractmethod


class HotCocoVendingMachine(ABC):
    def prepare(self):
        self.add_powder()
        self.brew()
        self.pour_into_cup()
        self.add_condiments()

    @abstractmethod
    def add_powder(self):
        pass

    def brew(self):
        print('steeping')

    def pour_into_cup(self):
        print('pour drink into cup')

    @abstractmethod
    def add_condiments(self):
        pass
