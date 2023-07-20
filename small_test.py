def create_map(ship_coordinates):
    """A function that takes as an argument list of player's ship coordinates and prints a map with X as ship mark"""
    grid = [['.' for _ in range(10)] for _ in range(10)]  # Create a 10x10 grid filled with dots

    for coordinate in ship_coordinates:
        column, row = coordinate
        if 0 <= column < 10 and 0 <= row < 10:  # Check if the coordinate is within the grid boundaries
            grid[row][column] = 'X'  # Place the ship at the specified coordinate

    # Print the map using nested for loops
    for column in grid:
        for row in column:
            print(row, end=' ')
        print()


def enter_coordinates():  # create any ship coordinates tuple

    fleet = []  # the fleet is empty in the beginning

    big_ship = []
    medium_ships = []
    small_ships = []

    min_allowed_value = 0
    max_allowed_value = 9
    
    while len(fleet) != 6:  # run the process until all ships are created

        # ask player for the size of the ship to create
        ship_size = int(input("Enter the size of the ship you want to create (5, 3 or 2): "))

        # validation for the ships limit
        if len(big_ship) == 1:
            print("You already have big ship, choose another size.")
            continue 
        elif len(medium_ships) == 2:
            print("You have reached the limit for medium ships.")
            continue 
        elif len(small_ships) == 3:
            print("You have reached the limit for small ships.") 
            continue  # stop the iteration and ask again if the player already created some type of ships

        print(f"Let's create the {ship_size} decks long ship!")

        ship_length = 0  # the length of the ship
        deck = 1  # how many decks ship has from the user perspective

        while ship_length != ship_size:  # ask user to enter coordinates until the ship has required size
            coordinates_column = int(input(f"Input column coordinate for the ship deck {deck} : "))
            coordinates_row = int(input(f"Input row coordinate for the ship deck {deck} : "))
            fleet.append((coordinates_column, coordinates_row))
            ship_length += 1
            deck += 1


        # for limit of ships  
        if ship_size == 5:
            big_ship.append(1)
            print("Big ship list: ", big_ship)
        elif ship_size == 3:
            medium_ships.append(1)
            print("Medium ships list: ", medium_ships)
        elif ship_size == 2:
            small_ships.append(1)
            print("Small ships list: ", small_ships)

        
            

    # validation for the input

    return fleet

        
coordinates = enter_coordinates()
print("Your fleet is completed")
create_map(coordinates)
