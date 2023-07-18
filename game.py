import random


def create_map(ship_coordinates):
    grid = [['.' for _ in range(10)] for _ in range(10)]  # Create a 10x10 grid filled with dots

    for coordinate in ship_coordinates:
        x, y = coordinate
        if 0 <= x < 10 and 0 <= y < 10:  # Check if the coordinate is within the grid boundaries
            grid[y][x] = 'X'  # Place the ship at the specified coordinate

    # Print the map using nested for loops
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()


def select_positions(coordinates):
    """a function that allows the user to select positions for their ships"""

    ship_coordinates = []
    for ship in range(fleet):
        valid_position = False
        while not valid_position:
            coordinate = input(f"Ahoy Captain! Enter the coordinates for ship {ship + 1} (x, y): ")
            try:
                x, y = map(int, coordinate.split(','))
                if 0 <= x < 10 and 0 <= y < 10:  # Check if the coordinate is within the grid boundaries
                    if (x, y) not in ship_coordinates:  # Check if the position is already taken
                        ship_coordinates.append((x, y))
                        valid_position = True
                    else:
                        print("Position already taken. Please select a different position.")
                else:
                    print("Position is out of the filed. Please enter values between 0 and 9.")
            except ValueError:
                print("Invalid input format. Please enter coordinates in the format 'x, y'.")

    return ship_coordinates


# number of ships is reduced for testing, change back after finishing
fleet = 2
player_fleet = select_positions(fleet)
create_map(player_fleet)


def create_computer_fleet(fleet):
    """a function that randomly places computer ships"""

    pc_ship_coordinates = []
    for ship in range(fleet):
        valid_position = False
        while not valid_position:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in pc_ship_coordinates:
                pc_ship_coordinates.append((x, y))
                valid_position = True

    return pc_ship_coordinates


fleet = 3
computer_ship_field = create_computer_fleet(fleet)
print("testing computer fleet: ", computer_ship_field)
