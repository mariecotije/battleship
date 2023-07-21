from create_map import *


def enter_coordinates():  # create any ship coordinates tuple

    fleet = []  # the fleet is empty in the beginning

    # lists for verification of the amount of concrete types
    big_ship = []
    medium_ships = []
    small_ships = []

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
        if ship_size == 5 and len(big_ship) == 1:
            print("You already have big ship, choose another size.")
            continue 
        elif ship_size == 3 and len(medium_ships) == 2:
            print("You have reached the limit for medium ships.")
            continue 
        elif ship_size == 2 and len(small_ships) == 3:
            print("You have reached the limit for small ships.") 
            continue  # stop the iteration and ask again if the player already created some type of ships

        print(f"Let's create the {ship_size} decks long ship!")

        ship_length = 0  # the length of the ship
        deck = 1  # how many decks ship has from the user perspective

        # create coordinates tuple
        # validation for the coordinates input
        while ship_length != ship_size:  # ask user to enter coordinates until the ship has required size
            try:
                coordinates_column = int(input(f"Input column coordinate for the ship deck {deck} : "))
                if coordinates_column < min_allowed_value or coordinates_column > max_allowed_value:
                    print("This position is out of grid. Insert number 0-9.")
                    continue
                coordinates_row = int(input(f"Input row coordinate for the ship deck {deck} : "))
                if coordinates_row < min_allowed_value or coordinates_row > max_allowed_value:
                    print("This position is out of grid. Insert number 0-9.")
                    continue
                if (coordinates_column, coordinates_row) not in fleet:  # if position is available, add to fleet
                    fleet.append((coordinates_column, coordinates_row))
                    ship_length += 1
                    deck += 1

                else:  # handling occupied position
                    print("You already placed ship there. Choose another position.")
                    continue
            except ValueError:  # handling incorrect input type
                print("Only numbers are allowed. Try again.")
                continue

        # conditions for limit of ships and informing player of the ships position

        if ship_size == 5:
            big_ship.append("X")
            print("Big ship: ", big_ship)
        elif ship_size == 3:
            medium_ships.append("X")
            print("Medium ships: ", medium_ships)
        elif ship_size == 2:
            small_ships.append("X")
            print("Small ships: ", small_ships)

    return fleet

        
coordinates = enter_coordinates()
create_map(coordinates)
