from iterator_interface import Iterator


class LunchIterator(Iterator):
    def __init__(self, item):
        self.item = item
        self.idx = 0

    def next(self):
        menu_item = self.item[self.idx]
        self.idx += 1
        return menu_item

    def has_next(self):
        return self.idx < len(self.item)


class DinnerIterator(Iterator):
    def __init__(self, item):
        self.item = item
        self.idx = 0

    def next(self):
        menu_item = list(self.item.values())[self.idx]
        self.idx += 1
        return menu_item

    def has_next(self):
        return self.idx < len(self.item)
