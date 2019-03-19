# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,startLocation):
        self.location = startLocation

    def change_location(self,changedLocation):
        self.location = changedLocation

    def print_location(self):
        print(self.location)

