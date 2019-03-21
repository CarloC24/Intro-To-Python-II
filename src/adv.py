from room import Room
from player import Player
from item_list import item_list
from multiline_commands import *



# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",item_list['book']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",item_list['torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",item_list['orb']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",item_list['lantern']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",item_list['sword']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



# Global Variables
print_room = True
#
# Main
#
def move_player(my_player, inp):
    new_room = my_player.location.get_location(inp)
    if new_room == None:
        print(' You cannot move on that direction')
        return False
    else:
        my_player.change_location(new_room)
        return True

multiline_command = {}
multiline_command['get'] = get_command
multiline_command['drop'] = drop_command
multiline_command['look'] = look_command


# Make a new player object that is currently in the 'outside' room.
my_player = Player(input('Please enter a name:'),room['outside'],[])
while True:
    if print_room:
        print(f'hey {my_player.name} you are at {my_player.location.name} \n {my_player.location.description}')
    inp = input('Please enter a direction :')
    inp = inp.split(' ')
    if inp[0] == 'q':
        break
    elif inp[0] == 'n' or inp[0] == 'w' or inp[0] == 's' or inp[0] == 'e':
       print_room =  move_player(my_player,inp[0])
    elif len(inp) > 1:
        multiline_command[inp[0]](inp,my_player)
        print_room = False
    else:
        print_room = False
        print('enter n for north w for west s for south e for east')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
