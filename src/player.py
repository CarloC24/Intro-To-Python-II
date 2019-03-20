# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self,name, startLocation,items):
        self.name = name
        self.location = startLocation
        self.items = items

    def change_location(self, changedLocation):
        self.location = changedLocation

    def print_location(self):
        print(f'you are at {self.location.name}')

    def print_items(self):
        if len(self.items):
            print(f'your items are {[x for x in self.items]}')
        else:
            print(f'you have no items in your inventory {self.name}')

    def add_or_remove(self,item):
        if item in self.items:
            print(f'successfully removed {item.name}')
            self.items.remove(item)
        else:
             print(f'successfully added {item.name}')
             self.items.append(item)

    def remove_item(self,item):
        self.items.remove(item)

    def add_item(self,item):
        self.items.append(item)
