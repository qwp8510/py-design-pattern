from menu_component import MenuComponent


class Menu(MenuComponent):

    def __init__(self, item_name, description):
        self.menu_components = []
        self.item_name = item_name
        self.description = description

    def add_child(self, menu_component):
        self.menu_components.append(menu_component)

    def remove_child(self, menu_component):
        del self.menu_components[self.menu_components.index(menu_component)]

    def get_child(self, idx):
        if idx > len(self.menu_components):
            print("index out of range")
            return
        self.menu_components[idx]

    def get_item_name(self):
        return self.item_name

    def get_description(self):
        return self.description

    def show(self):
        print(
            self.get_item_name(),
            self.get_description()
        )
        print('==================')
        for component in self.menu_components:
            component.show()
