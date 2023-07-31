import random


# create map for the player
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


# lists player's ships (global scope)

big_ship = []
medium_ships = []
small_ships = []


# create player fleet
def convert_coordinates(position_input):
    """A function that takes user input with inserted coordinates.
    If there is no letter in the coordinates input, both int are converted to tuple and returned.
    Column is converted from letter to number using 'switch'.
    Row is counted -1 to place according to rows indexes on the grid.
    Function returns tuple of coordinates that can be read by other functions for placing ships."""
    column = position_input[0]
    row = position_input[1:]
    row_int = int(row)  # convert string to int
    if column == int:
        map_coordinates = (column, (row - 1))  # create tuple for verification
    else:
        column = str(column.upper())  # convert user input to string and to uppercase for switch

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


def enter_coordinates():
    """A function for ships creation for player.
    A player is asked for an input to place ships on map.
    An input is converted to tuple and added to the list of ships based on the size.
    All ships are combined to the player's fleet.
    Function returns list of all ships coordinates as player's fleet."""

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

        print("Placed ships: ", placed_ships)

    return fleet


# create fleet for pc

computer_fleet = []  # a list for all coordinates to check occupied (global scope)

# lists for checking target size in the iteration (global scope)
pc_big_ship = []  # a list for big ship
pc_medium_ships = []  # a list for medium ships
pc_small_ships = []  # a list for small ships

# a list of coordinates around cell for making sure ships are not connected to each other
near_coordinates = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def first_coordinates():
    """A function that creates and returns a tuple of random coordinates (column, row)."""
    column = random.randint(0, 9)
    row = random.randint(0, 9)

    return column, row


def is_enough_space(ship_size, chosen_orientation, start_coordinates):
    """A function for verification whether a ship can fit on the grid based on the start coordinates,
    orientation and ship size."""

    (column, row) = start_coordinates
    grid_size = 10

    if chosen_orientation == "horizontal" and (grid_size - ship_size) < column:
        return False
    elif chosen_orientation == "vertical" and (grid_size - ship_size) < row:
        return False
    else:
        return True


def create_near_ship_coordinates(ship_coordinates):
    """A function that takes ship coordinates list as an argument and returns a list of coordinates around that ship.
    The function is then used for verification of already occupied space on the grid."""

    new_near_coordinates = []
    for coordinates in ship_coordinates:
        (column, row) = coordinates
        for close_coordinates in near_coordinates:
            (near_column, near_row) = close_coordinates
            new_near_coordinates.append(((column + near_column), (row + near_row)))

    return new_near_coordinates


def position_is_occupied(ship_coordinates):
    """A function that takes a list of ship coordinates as an argument and compares each tuple in the list
    with already created ships coordinates in the whole fleet.
    A boolean value is returned as a result."""

    near_ship_coordinates = create_near_ship_coordinates(ship_coordinates)
    for near_coordinate_tuple in near_ship_coordinates:
        if near_coordinate_tuple in computer_fleet:
            return True

    return False


def create_ship(ship_size):
    """A function that takes the ship size (int) value as an argument and returns a new list of coordinates.
    The returned list has length for the required ship size."""

    # ship coordinates holder
    new_ship = []

    # create start coordinates
    start_coordinates = first_coordinates()

    # choose orientation randomly
    orientation = ["vertical", "horizontal"]
    chosen_orientation = random.choice(orientation)

    # check if a ship can be created based on a size, orientation and start using 'is_enough_space' function
    while not is_enough_space(ship_size, chosen_orientation, start_coordinates):
        # create start coordinates
        start_coordinates = first_coordinates()

        # choose orientation
        orientation = ["vertical", "horizontal"]
        chosen_orientation = random.choice(orientation)

    # proceed with ship generation

    # unpack tuple and create ship using for loop
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


def create_computer_fleet():
    """ A function for creation full fleet for the computer.
    Function returns a list of all ships coordinates, that used later for iteration of moves."""

    # create and add big ship to the main list
    create_pc_big_ship = create_ship(5)
    pc_big_ship.extend(create_pc_big_ship)
    computer_fleet.extend(pc_big_ship)

    while len(pc_medium_ships) != 6:
        # create medium ships
        pc_medium_ship = create_ship(3)
        if position_is_occupied(pc_medium_ship):
            continue
        else:
            computer_fleet.extend(pc_medium_ship)
            pc_medium_ships.extend(pc_medium_ship)

    while len(pc_small_ships) != 6:
        pc_small_ship = create_ship(2)
        if position_is_occupied(pc_small_ship):
            continue
        else:
            pc_small_ships.extend(pc_small_ship)
            computer_fleet.extend(pc_small_ship)

    return computer_fleet


# checking size of the target for player

def check_player_target_size(coordinates):
    """A function that takes a tuple of coordinates as an input and shows the message to the player,
    based on the list this tuple is found.
    If coordinates are found in a list, they are removed from it."""

    if coordinates in pc_big_ship:
        print("You hit BIG ship of 5 decks!")
        pc_big_ship.remove(coordinates)
    elif coordinates in pc_medium_ships:
        print("Nice! MEDIUM size ship is damaged!")
        pc_medium_ships.remove(coordinates)
    elif coordinates in pc_small_ships:
        print("SMALL size ship was hit!")
        pc_small_ships.remove(coordinates)


# checking the player's fleet status

def check_pc_target_size(pc_shot):
    """A function for checking the size of the ship when computer hits.
    A coordinates tuple generated by computer is taken as an argument.
    If coordinates are fond in a list, message is printed for the player.
    Coordinates are removed from the list."""

    if pc_shot in big_ship:
        print("Oh no! Computer hit your BIG ship!")
        big_ship.remove(pc_shot)
    elif pc_shot in medium_ships:
        print("Your MEDIUM size ship was hit by computer!")
        medium_ships.remove(pc_shot)
    elif pc_shot in small_ships:
        print("Computer hit a SMALL size ship!")
        small_ships.remove(pc_shot)


# pc making shots strategy
pc_missed_shots = []
pc_successful_shots = []


def pc_random_shot():
    """A function for new random pair of coordinates for pc shot.
    Column and row numbers are chosen from the range 0-9 and put together as a tuple.
    Function returns a tuple (column, row)."""
    pc_choice_column = random.randint(0, 9)
    pc_choice_row = random.randint(0, 9)
    pc_shot = (pc_choice_column, pc_choice_row)  # creating tuple from both random inputs

    return pc_shot


# pc deciding where to make next shot in every iteration


def pc_next_column_forward():
    """A function for computer to make a shot next to last successful shot if it wasn't made yet.
    Last item is taken from the list and updated for move one column forward.
    A function returns updated tuple of coordinates for move to next column, but same row."""

    last_successful_shot = pc_successful_shots[-1]
    (column, row) = last_successful_shot
    new_column = (column + 1)
    next_column_forward_coordinates = (new_column, row)

    return next_column_forward_coordinates


def pc_next_row_down():
    """A function for computer to make a shot using last coordinates from the list of successful shots.
    If next column coordinates were already used, computer places a shot on the row below, but same column.
    Function returns new tuple with the same column, new row."""

    last_successful_shot = pc_successful_shots[-1]
    (column, row) = last_successful_shot
    new_row = (row + 1)
    next_row_down_coordinates = (column, new_row)

    return next_row_down_coordinates


def pc_decide_where_to_send_missiles():
    """A function for pc strategy where to make next shot based on the previous one.
    After checking conditions, it returns random pair of coordinates or next to previous successful shot.
    Decision is based on coordinates availability and length of the lists in the beginning."""

    if len(pc_successful_shots) == 0 and len(pc_missed_shots) == 0:  # first shot random
        pc_shot = pc_random_shot()
    elif len(pc_successful_shots) == 0:  # make random until there is at least one item in the list of good shots
        pc_shot = pc_random_shot()
    else:
        pc_shot = pc_next_column_forward()  # make shot next to the last good, one column forward
        if pc_shot in pc_successful_shots or pc_shot in pc_missed_shots:  # if coordinates were already used before
            pc_shot = pc_next_row_down()  # make shot one row down
            if pc_shot in pc_missed_shots:
                pc_shot = pc_random_shot()

    return pc_shot


# iteration of moves

# list of player's shot for the map to print after each round
player_successful_shots = []
player_missed_shots = []


# print map of shots for player
def show_already_made_player_shots(successful_shots, missed_shots):
    """An updated function for printing map of player's shots.
    A function takes 2 lists of coordinates as an argument and prints the grid
    For successful shots is placed 'X'. For missed shots 'O'."""

    print("*MAP OF YOUR PREVIOUS SHOTS*")

    # Print the header with letters from 'a' to 'j'
    print('   ', end='')  # Add an extra space for alignment
    for letter in 'ABCDEFGHIJ':
        print(letter, end=' ')
    print()

    grid = [['.' for row in range(10)] for column in range(10)]

    for coordinate in successful_shots:  # a for loop for successful shots
        column, row = coordinate
        if 0 <= column < 10 and 0 <= row < 10:  # Check if the coordinate is within the grid boundaries
            grid[row][column] = 'X'  # Place the sign at the hit ship

    for coordinate in missed_shots:  # a for loop for missed shots
        column, row = coordinate
        if 0 <= column < 10 and 0 <= row < 10:  # Check if the coordinate is within the grid boundaries
            grid[row][column] = 'O'  # Place the sign at the missed coordinate

    # Print the map using nested for loops
    for row_index, column in enumerate(grid):
        print(f"{row_index + 1:2}", end=' ')  # Print the row number with 2 characters (right-aligned)
        for row in column:
            print(row, end=' ')
        print()


def convert_pc_coordinates(pc_tuple_coordinates):
    (column, row) = pc_tuple_coordinates

    match column:
        case 0:
            column = "A"
        case 1:
            column = "B"
        case 2:
            column = "C"
        case 3:
            column = "D"
        case 4:
            column = "E"
        case 5:
            column = "F"
        case 6:
            column = "G"
        case 7:
            column = "H"
        case 8:
            column = "I"
        case 9:
            column = "J"

    converted_pc_coordinates = (column, (row + 1))

    return converted_pc_coordinates


def players_moves(computer_fleet, player_fleet):
    """A function for main iteration between players.
    Lists of player and computer's fleet are taken as input.
    User is making first move by entering 2 numbers (column, row) separated by space. Input is converted to tuple.
    If the tuple is in the list of the computer's fleet, the ship is destroyed and the tuple is removed from the list.
    Next move is for computer.
    Computer input is generated using 'pc_decide_where_to_send_missiles' function.
        If computer hits player's ship in the previous move, it moves 1 column or row forward.
        If next to successful coordinates were used, computer generates new random coordinates.
    The logic for destroyed ship is the same as for player's move.
    Iteration continues until one of the fleets is destroyed completely, means the list is empty."""

    # initial score for both players
    player_score = 0
    computer_score = 0

    # different messages to show when player hit the enemy ship
    messages = [
        "You missed",
        "Impressive shot, but missed",
        "No enemy ships there"
    ]
    # a list of already used coordinates for checking
    used_coordinates = []

    # main iteration loop
    while computer_fleet != 0 and player_fleet != 0:
        show_already_made_player_shots(player_successful_shots, player_missed_shots)
        try:  # user  input
            player_input = input("Enter target coordinates: ")
            coordinates = convert_coordinates(player_input)  # converting user input to tuple
            (column, row) = coordinates  # unpack tuple for verification
            if len(coordinates) < 2:  # prevent sending user input if not 2 coordinates
                print("Two coordinates are needed for shot. Try again.")
                continue
            elif column < 0 or column > 9 or row < 0 or row > 9:
                print("These coordinates are out of the map. Try again.")
                continue
            elif coordinates in used_coordinates:
                print("You already tried these coordinates. Insert another pair.")
                continue
        except ValueError:  # prevent app from failing when user inserts non integer
            print("Please enter target coordinates inside map, example: 'A1'.Try again.")
            continue
        else:
            if coordinates in computer_fleet:
                check_player_target_size(coordinates)
                computer_fleet.remove(coordinates)
                used_coordinates.append(coordinates)  # for checking already used coordinates
                player_successful_shots.append(coordinates)  # add to the list for map of shots
                player_score += 1
                print("Your score: ", player_score)
                if len(computer_fleet) == 0:
                    print("Congratulations! You sunk all the computer's ships! GAME OVER")
                    break
            elif coordinates not in computer_fleet:
                print(random.choice(messages))  # show a random message form the list
                used_coordinates.append(coordinates)  # for checking already used coordinates
                player_missed_shots.append(coordinates)  # add to the list for map of shots

        # computer's turn

        print(f"Computer is sending missiles...")
        pc_shot = pc_decide_where_to_send_missiles()
        converted_pc_shot_for_user = convert_pc_coordinates(pc_shot)
        if pc_shot in player_fleet:
            print(f"DAMN! Enemy strike at {converted_pc_shot_for_user} was successful!")
            player_fleet.remove(pc_shot)
            check_pc_target_size(pc_shot)
            computer_score += 1
            print("Computer score: ", computer_score)
            pc_successful_shots.append(pc_shot)  # add successful shot to the list for next iteration
            if len(player_fleet) == 0:
                print("Ay, caramba! Your fleet was destroyed!")
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {converted_pc_shot_for_user}")
            pc_missed_shots.append(pc_shot)  # add missed shot to the list for next iteration


# the main function for playing game

def play_battleship(start_game):
    """The main function where the player and computer iterate in guessing the opponent's ship location.
    A boolean value is taken as an argument for starting the game.
    Game starts with creation of ships for the player.
    Then all ships are created for computer.
    Iteration of moves is going until one of the fleets is destroyed."""

    # welcome message
    print("Ahoy Captain! Let's create your fleet!")
    print("Place your ships on the grid 10x10. Column indexes are A - H. Rows are 1 - 10.\n"
          "Your fleet must have: one ship for 5 decks, two ships for 3 decks and three ships for 2 decks.\n"
          "Check the map with already placed ships before creating next one.\n"
          "Insert coordinates like 'a1' or 'A1'\n"
          "Here is the grid for your ships.")
    create_map([])  # show the empty map to the player

    # create fleet for the player
    players_fleet = enter_coordinates()
    print("Your fleet is ready! Check the map.")
    create_map(players_fleet)  # create map after all ships are placed and show it to the player

    # fleet is created for pc
    computer_fleet = create_computer_fleet()
    print("Enemy fleet is ready for battle.\nYo Ho, Ho! Let's destroy some enemy ships!")

    # initial score for both players
    player_score = 0
    computer_score = 0

    # iteration of moves in guessing the opponent's ship location
    players_moves(computer_fleet, players_fleet)

    # clear all ships lists when game is over
    big_ship.clear()
    medium_ships.clear()
    small_ships.clear()
    players_fleet.clear()
    computer_fleet.clear()
    pc_big_ship.clear()
    pc_medium_ships.clear()
    pc_small_ships.clear()
    pc_missed_shots.clear()
    pc_successful_shots.clear()
    player_successful_shots.clear()
    player_missed_shots.clear()


# a function for playing game again util player ends it
def start_new_game():
    """The main function for starting game. When the game is over, the function asks user for input,
        to start another round.
    Start game boolean is sent as an argument to the play_battleship function."""
    start_game = True

    while start_game:  # a loop for starting new game
        play_battleship(start_game)
        ask_player = str(input("Do you want to play again? Enter any character for YES or 'n' for NO: "))
        if ask_player == "n":
            print("Thank you for playing! Good bye!")  # exit the game by command from player
            break


# launch game
start_new_game()
