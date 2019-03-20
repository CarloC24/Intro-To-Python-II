# Implement a class to hold room information. This should have name and
# description attributes.
from item_list import item_list


class Room:
    def __init__(self, name, description,items):
        self.name = name
        self.description = description
        self.items = [items]
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None

    def get_location(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'w':
            return self.w_to
        if direction == 'e':
            return self.e_to

    def print_items(self):
        if self.items:
             print([x.name for x in self.items])
        else:
            print('There are no items in the room')

    def add_or_remove(self,item):
        print(f'these are the items {self.items}')
        if item in [x.name for x in self.items]:
            print(f'successfully added {item} to your inventory')
            self.items.remove(item_list[item])
        else:
             print(f'successfully added {item}')
             self.items.append(item_list[item])

    def check_item(self,item):
        if item in [x.name for x in self.items]:
            return True
        else:
            return False