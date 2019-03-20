# Implement a class to hold room information. This should have name and
# description attributes.


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
        print([x.name for x in self.items])

    def add_or_remove(self,item):
        if item in self.items:
            print(f'successfully removed {item.name}')
            self.items.remove(item)
        else:
             print(f'successfully added {item.name}')
             self.items.append(item)

    def check_item(self,item):
        if item in [x.name for x in self.items]:
            return True
        else:
            return False