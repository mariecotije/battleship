from create_map import create_map


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


big_ship = []
medium_ships = []
small_ships = []


def enter_coordinates():  # create any ship coordinates tuple

    # lists for verification of the amount of concrete types
    fleet = []
    placed_ships = []  # a list for player to show already used coordinates

    ships = [2, 3, 5]  # list of ship sizes for verification of input ship_size

    min_allowed_value = 0
    max_allowed_value = 9

    while len(fleet) != 17:  # run the process until all ships are created

        # ask player for the size of the ship to create
        # validation for the ship size input
        try:
            ship_size = int(input("Enter the size of the ship you want to create (5, 3 or 2): "))
        except ValueError:  # if user inserts non integer
            print("Only numbers 5, 3 and 2 are allowed. Try again.")
            continue
        else:  # if the user inserts incorrect size number
            if ship_size not in ships:
                print(f"The {ship_size} size is not allowed. Choose the correct size.")
                continue

        # validation for the ships amount limit
        if ship_size == 5 and len(big_ship) == 5:
            print("You already have big ship, choose another size.")
            continue
        elif ship_size == 3 and len(medium_ships) == 6:
            print("You have reached the limit for medium ships. Choose another size.")
            continue
        elif ship_size == 2 and len(small_ships) == 6:
            print("You have reached the limit for small ships.Choose another size.")
            continue  # stop the iteration and ask again if the player already created some type of ships

        print(f"Let's create the {ship_size} decks long ship!")

        ship_length = 0  # the length of the ship
        deck = 1  # how many decks ship has from the user perspective

        # create coordinates tuple
        # validation for the coordinates input
        while ship_length != ship_size:  # ask user to enter coordinates until the ship has required size
            try:
                deck_coordinates = input(f"Input coordinate for the ship deck {deck} : ")
                converted_coordinates = convert_coordinates(deck_coordinates)
                print("Converted coordinates: ", converted_coordinates)
                (column, row) = converted_coordinates

                if column < min_allowed_value or column > max_allowed_value:
                    print("This position is out of grid. Choose another position.")
                    continue

                elif row < min_allowed_value or row > max_allowed_value:
                    print("This position is out of grid. Choose another position.")
                    continue

                if converted_coordinates not in fleet:  # if position is available, add to fleet
                    if ship_size == 5:
                        big_ship.append(converted_coordinates)
                    elif ship_size == 3:
                        medium_ships.append(converted_coordinates)
                    elif ship_size == 2:
                        small_ships.append(converted_coordinates)

                    ship_length += 1
                    deck += 1

                    fleet = big_ship + medium_ships + small_ships  # join all lists to one for iteration
                    placed_ships.append(deck_coordinates)
                    create_map(fleet)

                else:  # handling occupied position
                    print("You already placed ship there. Choose another position.")
                    continue
            except ValueError:  # handling incorrect input type
                print("Enter position with both coordinates like 'a1'. Try again.")
                continue

        print("Fleet: ", fleet)

        print("Placed ships: ", placed_ships)

    return fleet

        
coordinates = enter_coordinates()
create_map(coordinates)
