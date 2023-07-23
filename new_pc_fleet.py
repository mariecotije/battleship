from create_map import *
import random


def first_coordinates():
    """A function that randomly creates a tuple of coordinates"""
    column = random.randint(0, 9)
    row = random.randint(0, 9)

    return column, row


def is_enough_space(ship_size, chosen_orientation, start_coordinates):
    # a check whether a ship can fit based on the start coordinates, orientation and ship size
    (column, row) = start_coordinates

    if ship_size == 5 and chosen_orientation == "horizontal" and column <= 5:
        return True
    elif ship_size == 3 and chosen_orientation == "horizontal" and column <= 7:
        return True
    elif ship_size == 2 and chosen_orientation == "horizontal" and column <= 8:
        return True
    elif ship_size == 5 and chosen_orientation == "vertical" and row <= 5:
        return True
    elif ship_size == 3 and chosen_orientation == "horizontal" and row <= 7:
        return True
    elif ship_size == 2 and chosen_orientation == "horizontal" and row <= 8:
        return True
    else:
        return False


def position_not_occupied(ship):
    pass


def create_ship(ship_size):
    # ship coordinates holder
    new_ship = []

    # create start coordinates
    start_coordinates = first_coordinates()

    # choose orientation
    orientation = ["vertical", "horizontal"]
    chosen_orientation = random.choice(orientation)

    # check if coordinates are ok
    while not is_enough_space(ship_size, chosen_orientation, start_coordinates):
        # create start coordinates
        start_coordinates = first_coordinates()

        # choose orientation
        orientation = ["vertical", "horizontal"]
        chosen_orientation = random.choice(orientation)

    # proceed with ship generation

    # unpack tuple and create ship
    (column, row) = start_coordinates
    if chosen_orientation == "vertical":
        for ship in range(ship_size):
            new_ship.append((column, row))
            row += 1

    elif chosen_orientation == "horizontal":
        for ship in range(ship_size):
            new_ship.append((column, row))
            column += 1

    return new_ship


def create_pc_fleet():
    print("Adding new ships to the fleet")

    pc_big_ship = create_ship(5)
    print("Big ship created: ", pc_big_ship)

    pc_medium_ships = []
    for fleet in range(2):
        pc_medium_ship = create_ship(3)
        pc_medium_ships.extend(pc_medium_ship)
    print("Medium ships created: ", pc_medium_ships)

    pc_small_ships = []
    for fleet in range(3):
        pc_small_ship = create_ship(2)
        pc_small_ships.extend(pc_small_ship)
    print("Small ships created: ", pc_small_ships)

    pc_fleet = []

    occupied = False
    while not occupied:
        pc_fleet.extend(pc_big_ship)
        occupied = True
        pc_fleet.extend(pc_medium_ships)
        occupied = True
        pc_fleet.extend(pc_small_ships)
        occupied = True
        if pc_big_ship or pc_medium_ships or pc_small_ships in pc_fleet:
            occupied = True
            print("Position occupied, creating new ship.")
            continue

    return pc_fleet


pc_fleet = create_pc_fleet()
print(pc_fleet)
create_map(pc_fleet)







