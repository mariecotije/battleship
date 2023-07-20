import random

def create_computer_fleet():
    """A function that places computer ships using random method.
    If place is occupied, it tries again until fleet is completed"""

    computer_fleet = []
    for ship in range(2):  # same size of the fleet
        valid_position = False
        while not valid_position:
            column = random.randint(0, 9)
            row = random.randint(0, 9)
            if (column, row) not in computer_fleet:
                computer_fleet.append((column, row))  # adding a coordinates tuple to the list
                valid_position = True

    return computer_fleet