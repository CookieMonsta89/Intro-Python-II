# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, items=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items

    def move(self, direction):
        if direction == "n":
            self.currentRoom = self.currentRoom.n_to
        if direction == "s":
            self.currentRoom = self.currentRoom.s_to
        if direction == "e":
            self.currentRoom = self.currentRoom.e_to
        if direction == "w":
            self.currentRoom = self.currentRoom.w_to

    def itemInteraction(self, action):
        if action == 'p':
            self.items.append(self.currentRoom.items) 
        if action == 'r':
            self.items.clear()