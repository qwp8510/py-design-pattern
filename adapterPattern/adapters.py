from birds import BirdInterface


class DuckAdapter(BirdInterface):
    def __init__(self, duck):
        self.duck = duck

    def fly(self):
        self.duck.fly()

    def tweet(self):
        self.duck.quack()
