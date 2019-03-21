# Write a class to hold player information, e.g. what room they are in
# currently.
from item_list import item_list


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
            my_items = [x.name for x in self.items]
            print(f'your items are {my_items}')
        else:
            print(f'you have no items in your inventory {self.name}')

    def add_or_remove(self,item):
        if item in [x.name for x in self.items]:
            print(f'successfully removed {item} in your inventory in player.py')
            self.items.remove(item_list[item])
        else:
             print(f'successfully added {item} in your inventory in player.py')
             self.items.append(item_list[item])
    def add_item(self,item):
        if self.check_item(item):
            print('player already has that item')
        else:
            self.items.append(item_list[item])
    def remove_item(self,item):
        if self.check_item(item):
            self.items.remove(item_list[item])
        else:
            print(f'Cant remove item {item} because you dont have it')
    def check_item(self,item):
        if item in [x.name for x in self.items]:
            return True
        else:
            return False