# this is the multiline command file
from room import Room
from player import Player

def get_command(inp,my_player):
    print('you are at the get_command')

def drop_command(inp,my_player):
    print('you are at the drop_command')

def look_command(inp,my_player):
    if inp[1] == 'inventory':
        my_player.print_items()
    if inp[1] == 'items':
        print('shet')
        my_player.location.print_items()

