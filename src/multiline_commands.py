# this is the multiline command file
from room import Room
from player import Player
from item_list import item_list

def addroomitem_removeplayeritem(inp,item_list,my_player):
    if inp[1] in item_list:
            if my_player.location.check_item(inp[1]):
                my_player.location.add_item(inp[1])
                my_player.remove_item(inp[1])
            else:
                print(f'{inp[1]} is not in the room')
    else:
            print(f'the item {inp[1]} does not exist')

def addplayeritem_removeroomitem(inp,item_list,my_player):
    if inp[1] in item_list:
            if my_player.location.check_item(inp[1]):
                my_player.location.remove_item(inp[1])
                my_player.add_item(inp[1])
            else:
                print(f'{inp[1]} is not in the room')
    else:
            print(f'the item {inp[1]} does not exist')



def get_command(inp,my_player):
    if inp[1]:
        addplayeritem_removeroomitem(inp,item_list,my_player)
    else:
        print('type in the command help')

def drop_command(inp,my_player):
    if inp[1]:
       addroomitem_removeplayeritem(inp,item_list,my_player)
    else:
        print('type in the command help')

def look_command(inp,my_player):
    if inp[1] == 'inventory' or inp[1] == 'i':
        my_player.print_items()
    elif inp[1] == 'items':
        my_player.location.print_items()
    else:
        print('type in the command help')
