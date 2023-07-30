from create_map import create_map
import random

pc_fleet = []  # a list for all coordinates to check occupied

# lists for checking target size in the iteration
pc_big_ship = []  # a list for big ship
pc_medium_ships = []  # a list for medium ships
pc_small_ships = []  # a list for small ships

near_coordinates = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def first_coordinates():
    """A function that randomly creates a tuple of coordinates"""
    column = random.randint(0, 9)
    row = random.randint(0, 9)

    return column, row


def is_enough_space(ship_size, chosen_orientation, start_coordinates):
    # a check whether a ship can fit on the grid based on the start coordinates, orientation and ship size
    (column, row) = start_coordinates
    grid_size = 10

    if chosen_orientation == "horizontal" and (grid_size - ship_size) < column:
        return False
    elif chosen_orientation == "vertical" and (grid_size - ship_size) < row:
        return False
    else:
        return True


def create_near_ship_coordinates(ship_coordinates):
    new_near_coordinates = []
    for coordinates in ship_coordinates:
        (column, row) = coordinates
        for close_coordinates in near_coordinates:
            (near_column, near_row) = close_coordinates
            new_near_coordinates.append(((column + near_column), (row + near_row)))

    return new_near_coordinates


def position_is_occupied(ship_coordinates):
    """A function that checks coordinates in the whole fleet and returns response"""
    near_ship_coordinates = create_near_ship_coordinates(ship_coordinates)
    for near_coordinate_tuple in near_ship_coordinates:
        if near_coordinate_tuple in pc_fleet:
            return True

    return False


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

    # create and add big ship to the main list
    pc_big_ship = create_ship(5)
    pc_fleet.extend(pc_big_ship)
    print("Big ship created: ", pc_big_ship)

    while len(pc_medium_ships) != 6:
        # create medium ships
        pc_medium_ship = create_ship(3)
        if position_is_occupied(pc_medium_ship):
            print("Position is occupied. Next loop.")
            continue
        else:
            pc_fleet.extend(pc_medium_ship)
            pc_medium_ships.extend(pc_medium_ship)

    print("Medium ships created: ", pc_medium_ships)

    while len(pc_small_ships) != 6:
        pc_small_ship = create_ship(2)
        if position_is_occupied(pc_small_ship):
            print("Position is occupied. Next loop.")
            continue
        else:
            pc_small_ships.extend(pc_small_ship)
            pc_fleet.extend(pc_small_ship)

    print("Small ships created: ", pc_small_ships)

    return pc_fleet


def main():
    pc_fleet = create_pc_fleet()
    print(pc_fleet)
    create_map(pc_fleet)


main()
