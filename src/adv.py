from room import Room
from player import Player
from item import Item
from colorama import init
init()
# Declare all the rooms

room = {
    'outside':  Room("You are outside Cave Entrance",
                     "North of you, the cave mouth beckons for you.", ['hatchet', 'pipe', 'taco']),   
               

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'hatchet': Item('hatchet', 'rusty')
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
    # set current location to outside


player = Player("Joe", room['outside'])

print('\33[93m' + str(player) + '\33[0m')

currentRoom = room['outside']

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
player_input = None

backpack = ('\33[92m' + 'Backpack:' + '\33[0m')
location = ('\33[92m' + 'Location:' + '\33[0m')
itemsinroom = ('\33[92m' + 'Items in room:' + '\33[0m')
descriptionofroom = ('\33[92m' + 'Description:' + '\33[0m')
directionchoice = ('\33[94m' + 'north, south, east, west' + '\33[0m')

while (player_input is not 'q'):
    print(f"{backpack} {player.items}\n{location} {player.currentRoom.name}\n{descriptionofroom} {player.currentRoom.description}\n{itemsinroom} {player.currentRoom.items}.\nPlease pick a direction to go in ({directionchoice}).\nOr you can pick up an item using (p) or 'get itemname'")
    player_input = input("Enter the direction you'd like to go or grab an item:")
    previous_room = player.currentRoom
    if player_input != "p" and player_input != "r":
        player.move(player_input)
    if player_input.startswith("go ") or player_input.startswith("move "):
        direction = player_input.split(' ')
        player.move(direction[1])
    if player_input.startswith("get ") or player_input.startswith("grab ") or player_input.startswith("pickup "):
        items = player_input.split(' ')
        player.pickup(items[1])
    if player_input.startswith("drop "):
        items = player_input.split(' ')
        player.drop(items[1])
    elif player_input == 'p':
        player_input = input("what you wanna grab?")
        player.pickup(player_input)
    elif player_input == 'r':
        player_input = input("What you wanna drop?")
        player.drop(player_input)
    if player.currentRoom == None:
        print("You can't do that idiot!")
        player.currentRoom = previous_room
    

