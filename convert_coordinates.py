def convert_coordinates(position_input):
    """A function that takes as an argument tuple with inserted coordinates.
    A tuple is unpacked. Column is converted from letter to number using 'switch'.
    Column is counted -1 according to position on the grid.
    Function returns tuple of coordinates that can be read by other functions for placing ships."""

    (column, row) = position_input  # unpack tuple inserted by user
    row_int = int(row)  # convert string to int
    match column:  # switch for column converter
        case "A":  # convert letter to number
            column = 0
        case "B":
            column = 1
        case "C":
            column = 2
        case "D":
            column = 3
        case "E":
            column = 4
        case "F":
            column = 5
        case "G":
            column = 6
        case "H":
            column = 7
        case "I":
            column = 8
        case "J":
            column = 9
        case _:
            print("Out of range")

    map_coordinates = (column, (row_int - 1))  # create a tuple for coordinates on the grid, move row index

    return map_coordinates


position = tuple(input("Enter coordinates: "))
print(convert_coordinates(position))
