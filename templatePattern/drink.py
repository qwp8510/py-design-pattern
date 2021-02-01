from abc import ABC, abstractmethod


class BaseDrink(ABC):
    def prepare(self):
        self.add_powder()
        self.brew()
        self.pour_into_cup()
        if self.want_condiments():
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

    def want_condiments(self):
        return True


class Coco(BaseDrink):
    def add_powder(self):
        print('add coco powder')

    def add_condiments(self):
        print('add nothing')

    def want_condiments(self):
        return False


class Coffee(BaseDrink):
    def add_powder(self):
        print('add coffee powder')

    def add_condiments(self):
        print('add suger')

    def want_condiments(self):
        answer = input('do you want sugar?')
        if answer == 'n' or answer == 'N':
            return False
        else:
            return True
