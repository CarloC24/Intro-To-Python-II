# this is the multiline command file
from room import Room
from player import Player
from item_list import item_list

def additem_removeitem(inp,item_list,my_player):
    if inp[1] in item_list:
            if my_player.location.check_item(inp[1]):
                my_player.location.add_or_remove(inp[1])
                my_player.add_or_remove(inp[1])
            else:
                print(f'{inp[1]} is not in the room')
    else:
            print(f'the item {inp[1]} does not exist')



def get_command(inp,my_player):
    if inp[1]:
        additem_removeitem(inp,item_list,my_player)
    else:
        print('type in the command help')

def drop_command(inp,my_player):
    if inp[1]:
        if item_list[inp[1]]:
            print(item_list[inp[1]])
        else:
            print(f'no item found {item_list[inp[1]]}')
    else:
        print('type in the command help')

def look_command(inp,my_player):
    if inp[1] == 'inventory' or inp[1] == 'i':
        my_player.print_items()
    elif inp[1] == 'items':
        my_player.location.print_items()
    else:
        print('type in the command help')
