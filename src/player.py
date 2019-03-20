# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, startLocation,items):
        self.location = startLocation
        self.items = items

    def change_location(self, changedLocation):
        self.location = changedLocation

    def print_location(self):
        print(f'you are at {self.location.name}')

    def print_items(self):
        print(f'your items are {self.items}')
