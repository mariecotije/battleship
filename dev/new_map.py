all_ships_coordinates = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 5), (5, 6)]


def create_battleship_map(ship_coordinates):
    """A function that takes a list of coordinate pairs as an input and prints map with placed ships."""
    grid = [["." for column in range(10)] for row in range(10)]  # main list of lists

    for coordinates_pair in ship_coordinates:
        column, row = coordinates_pair
        # Check if the coordinates are within the grid boundaries
        if 0 <= column < 10 and 0 <= row < 10:
            # Place the ship on the grid by replacing the dot with 'X'
            grid[row][column] = 'X'

    # Print the map using nested for loops
    for column in grid:
        for row in column:
            print(row, end="")
        print()  # print empty space at the end of each inner for loop

    return grid


create_battleship_map(all_ships_coordinates)
