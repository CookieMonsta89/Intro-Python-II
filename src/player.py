# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, items=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items

    def __str__(self):
        return f"Greetings {self.name}!\n"

    def move(self, direction):
        if direction == "n" or direction == "north":
            self.currentRoom = self.currentRoom.n_to
        if direction == "s" or direction == "south":
            self.currentRoom = self.currentRoom.s_to
        if direction == "e" or direction == "east":
            self.currentRoom = self.currentRoom.e_to
        if direction == "w" or direction == 'west':
            self.currentRoom = self.currentRoom.w_to

    def pickup(self, action):
        if action in self.currentRoom.items:
            self.items.append(action)
            self.currentRoom.items.remove(action)

    def drop(self, action):
        if action in self.items:
            self.items.remove(action)
            self.currentRoom.items.append(action)