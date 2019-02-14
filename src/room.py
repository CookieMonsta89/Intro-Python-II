# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items # room will contain an array of items for player to interact with
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
        # setting directions equal to None

    def __str__(self):
        return f"{self.name}, {self.description}, {self.items}"

        # string function that just returns name, description and list of items