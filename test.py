def create_player_fleet():
    """A function that asks player for ship coordinates one by one and returns a list of all ships coordinates.
    The list is used for map"""

    ship_coordinates = [[big_ship], [medium_ships], [small_ships]]
    num_ships = 0  # total number of ships in the fleet
    big_ship = []  # one ship with 5 spaces
    medium_ships = []  # two ships with 3 spaces
    small_ships = []  # three ships with 2 spaces

    for ship in range(5):  # creating the biggest ship in the fleet
        cruiser_coordinates_column = int(input("Input coorinates for the cruiser (column)"))
        cruiser_coordinates_row = int(input("Input coorinates for the cruiser (row)"))
        big_ship.append((cruiser_coordinates_column, cruiser_coordinates_row))
        
    # creating medium ships
    for coordinates in range(6):
        medium_coordinates_column = int(input("Input coorinates for the cruiser (column): "))
        medium_coordinates_row = int(input("Input coorinates for the cruiser (row): "))
        medium_ships.append((medium_coordinates_column, medium_coordinates_row))

    # creating small ships
    for coordinates in range(6):
        small_coordinates_column = int(input("Input coorinates for the cruiser (column): "))
        small_coordinates_row = int(input("Input coorinates for the cruiser (row): "))
        small_ships.append((small_coordinates_column, small_coordinates_row))


    if coordinates in ship_coordinates:
        print("You already have ships there. Choose another position.")
        continue

    
    return ship_coordinates


print(create_player_fleet())