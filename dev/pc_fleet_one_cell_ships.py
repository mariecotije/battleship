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


def computer_ships():

    pc_big_ship = []
    pc_medium_ship = []
    pc_small_ship = []

    ship_sizes = [5, 3, 3, 2, 2, 2]

    computer_ships = []
    # create big ship
    while len(computer_ships) < 17:  # all ships coordinates
        ship_size = random.choice(ship_sizes)  # choose size from the list
        ship_sizes.remove(ship_size)  # remove chosen number from the list
        if len(pc_big_ship) == 5:
            continue
        elif len(pc_medium_ship) == 6:
            continue
        elif len(pc_small_ship) == 6:
            continue

        for ship in range(ship_size):
            column = random.randint(0, 9)
            row = random.randint(0, 9)
            if ship_size == 5:
                pc_big_ship.append((column, row))
            elif ship_size == 3:
                pc_medium_ship.append((column, row))
            elif ship_size == 2:
                pc_small_ship.append((column, row))

    computer_ships = pc_small_ship + pc_medium_ship + pc_big_ship
    return computer_ships


print(computer_ships())
