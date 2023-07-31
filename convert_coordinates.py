def convert_coordinates(position_input):
    """A function that takes user input with inserted coordinates saved in a variable as an argument.
    If there is no letter in the coordinates input, both int are converted to tuple and returned.
    Column is converted from letter to number using 'switch'.
    Row is counted -1 according to position on the grid.
    Function returns tuple of coordinates that can be read by other functions for placing ships."""
    column = position_input[0]
    row = position_input[1:]
    row_int = int(row)  # convert string to int
    if column == int:
        map_coordinates = (column, (row - 1))
    else:
        column = str(column.upper())

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

        map_coordinates = (int(column), (row_int - 1))  # create a tuple for coordinates on the grid, move row index

    return map_coordinates


deck_coordinates = input(f"Input coordinate for the ship deck : ")
converted_coordinates = convert_coordinates(deck_coordinates)
print("Converted coordinates: ", converted_coordinates)
