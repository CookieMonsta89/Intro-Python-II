from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("You are outside Cave Entrance",
                     "North of you, the cave mounth beckons for you."),

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
currentLocation = room['outside']
    # allows user to input their name
name = input('What do you call yourself?\n')
    # displays users name
player = Player(name, currentLocation, None)

def description(param):
    print(f"\nI've heard a lot about you {player.name}. {currentLocation}")

playerDirection = ''

playerDirection = input("What direction should we go?\n"
        "N for North, S for South, E for East or W for West")

if playerDirection == "N" or playerDirection == "S" or playerDirection == "E" or playerDirection == "W" or playerDirection == "Q" or playerDirection == "q":
    try:
        if playerDirection == "N":
            nextDirection = currentLocation.n_to
        if playerDirection == "S":
            nextDirection = currentLocation.s_to
        if playerDirection == "E":
            nextDirection = currentLocation.e_to
        if playerDirection == "W":
            nextDirection = currentLocation.w_to
    except AttributeError:
        print("You can't go that way!!")
        currentLocation = room['outside']
        playerDirection = input("So please choose either N, S, E, W or you can quit like a quitter and hit q\n")
            
    if nextDirection: currentLocation = nextDirection

    else:
        print("Wrong input idiot. Please use N, S, E, W")
        playerDirection = input("Will you please use N, S, E, W. You are driving me insane")



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
