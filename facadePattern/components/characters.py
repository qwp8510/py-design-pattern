class OfficeWorker():
    def __init__(self, name):
        self.name = name

    def eat(self, meal):
        """ Implement eat behavior """
        print('{} eat {}'.format(self.name, meal))
