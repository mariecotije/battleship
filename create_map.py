# ship_coordinates = [(1, 2), (1, 3), (6, 9), (7, 9), (6, 5), (7, 5)]


def create_map(ship_coordinates):
    """A function that takes as an argument list of player's ship coordinates and prints a map with X as ship mark"""

    # Print the header with letters from 'a' to 'j'
    print('   ', end='')  # Add an extra space for alignment
    for letter in 'ABCDEFGHIJ':
        print(letter, end=' ')
    print()

    grid = [['.' for row in range(10)] for column in range(10)]  # Create a 10x10 grid filled with dots

    for coordinate in ship_coordinates:
        column, row = coordinate
        if 0 <= column < 10 and 0 <= row < 10:  # Check if the coordinate is within the grid boundaries
            grid[row][column] = 'X'  # Place the ship at the specified coordinate

    # Print the map using nested for loops
    for row_index, column in enumerate(grid):
        print(f"{row_index + 1:2}", end=' ')  # Print the row number with 2 characters (right-aligned)
        for row in column:
            print(row, end=' ')
        print()


# ship_coordinates = [(1, 2), (1, 3), (6, 9), (7, 9), (6, 5), (7, 5)]
# create_map(ship_coordinates)


