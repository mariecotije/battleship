import random


# create map for the player
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


# player's ships

big_ship = []
medium_ships = []
small_ships = []


# create player fleet
def enter_coordinates():  # create any ship coordinates tuple

    # lists for verification of the amount of concrete types
    fleet = []

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
            print("You have reached the limit for medium ships.")
            continue
        elif ship_size == 2 and len(small_ships) == 6:
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
                    if ship_size == 5:
                        big_ship.append((coordinates_column, coordinates_row))
                    elif ship_size == 3:
                        medium_ships.append((coordinates_column, coordinates_row))
                    elif ship_size == 2:
                        small_ships.append((coordinates_column, coordinates_row))

                    ship_length += 1
                    deck += 1

                    fleet = big_ship + medium_ships + small_ships  # join all lists to one for iteration

                else:  # handling occupied position
                    print("You already placed ship there. Choose another position.")
                    continue
            except ValueError:  # handling incorrect input type
                print("Only numbers are allowed. Try again.")
                continue
        print("Fleet: ", fleet)

    return fleet


# create fleet for pc

computer_fleet = []  # a list for all coordinates to check occupied

# lists for checking target size in the iteration
pc_big_ship = []  # a list for big ship
pc_medium_ships = []  # a list for medium ships
pc_small_ships = []  # a list for small ships


def first_coordinates():
    """A function that randomly creates a tuple of coordinates"""
    column = random.randint(0, 9)
    row = random.randint(0, 9)

    return column, row


def is_enough_space(ship_size, chosen_orientation, start_coordinates):
    # a check whether a ship can fit on the grid based on the start coordinates, orientation and ship size
    (column, row) = start_coordinates
    grid_size = 10

    if chosen_orientation == "horizontal" and (grid_size - ship_size) < column:
        return False
    elif chosen_orientation == "vertical" and (grid_size - ship_size) < row:
        return False
    else:
        return True


def position_is_occupied(ship_coordinates):
    """A function that checks coordinates in the whole fleet and returns response"""

    for coordinates in ship_coordinates:
        if coordinates in computer_fleet:
            print(f"{ship_coordinates} is in fleet list")
            return True
    return False


def create_ship(ship_size):
    # ship coordinates holder
    new_ship = []

    # create start coordinates
    start_coordinates = first_coordinates()

    # choose orientation
    orientation = ["vertical", "horizontal"]
    chosen_orientation = random.choice(orientation)

    # check if coordinates are ok
    while not is_enough_space(ship_size, chosen_orientation, start_coordinates):
        # create start coordinates
        start_coordinates = first_coordinates()

        # choose orientation
        orientation = ["vertical", "horizontal"]
        chosen_orientation = random.choice(orientation)

    # proceed with ship generation

    # unpack tuple and create ship
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
    if coordinates in pc_big_ship:
        print("You hit big ship of 5 decks!")
        pc_big_ship.remove(coordinates)
    elif coordinates in pc_medium_ships:
        print("Nice! Medium ship is damaged!")
        pc_medium_ships.remove(coordinates)
    elif coordinates in pc_small_ships:
        print("Small ship is hit!")
        pc_small_ships.remove(coordinates)


# checking the player's fleet status

def check_pc_target_size(pc_shot):
    if pc_shot in big_ship:
        print("Oh no! Computer hit your biggest ship!")
        big_ship.remove(pc_shot)
    elif pc_shot in medium_ships:
        print("Your medium size ship was hit by computer!")
        medium_ships.remove(pc_shot)
    elif pc_shot in small_ships:
        print("Computer hit a small ship!")
        small_ships.remove(pc_shot)


# iteration of moves

def players_moves(computer_fleet, player_fleet):
    """A function for main iteration between players.
    User is making first move by inserting 2 numbers separated by space. Input is converted to tuple.
    If the tuple is in the list of the user's fleet, the ship is destroyed and the tuple is removed from the list.
    Next move is for computer.
    Computer input is generated tuple from 2 random integers. The same logic for destroyed ship.
    Iteration continues until one of the fleets is destroyed completely, means the list is empty."""

    # initial score for both players
    player_score = 0
    computer_score = 0

    # messages to show when player hit the enemy ship
    messages = [
        "You missed",
        "Impressive shot, but missed",
        "No enemy ships there"
    ]

    used_coordinates = []
    # main iteration loop
    while computer_fleet != 0 and player_fleet != 0:
        try:
            player_input = input("Enter two space separated numbers 0-9 and press Enter: ")  # user  input
            coordinates = tuple(int(number) for number in player_input.split())  # converting user input to tuple
            if len(coordinates) < 2:  # prevent sending user input if not 2 coordinates
                print("Two coordinates are needed for shot. Try again.")
                continue
            elif coordinates in used_coordinates:
                print("You already tried these coordinates. Insert another pair.")
                continue
        except ValueError:  # prevent app from failing when user inserts non integer
            print("Please enter 2 space separated numbers in range 0-9.")
            continue
        else:
            if coordinates in computer_fleet:
                check_player_target_size(coordinates)
                computer_fleet.remove(coordinates)
                used_coordinates.append(coordinates)  # for checking already used coordinates
                player_score += 1
                print("Your score: ", player_score)
                if len(computer_fleet) == 0:
                    print("Congratulations! You sunk all the computer's ships! GAME OVER")
                    break
            elif coordinates not in computer_fleet:
                print("Your shot: ", coordinates)
                print(random.choice(messages))  # show a random message form the list
                used_coordinates.append(coordinates)  # for checking already used coordinates

        # computer turn
        pc_choice_column = random.randint(0, 9)
        pc_choice_row = random.randint(0, 9)
        pc_shot = (pc_choice_column, pc_choice_row)  # creating tuple from both random inputs
        print(f"Computer is sending missiles...")
        if pc_shot in player_fleet:
            print(f"Damn! Enemy strike at {pc_shot} was successful!")
            player_fleet.remove(pc_shot)
            check_pc_target_size(pc_shot)
            computer_score += 1
            print("Computer score: ", computer_score)
            if len(player_fleet) == 0:
                print("Ay, caramba! Your fleet was destroyed!")
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {pc_shot}")


# the main function for playing game

def play_battleship(start_game):
    """a main function where the player and computer iterate in guessing the opponent's ship location"""

    # welcome message
    print("Ahoy Captain! Let's create your fleet!")

    # initial score for both players
    player_score = 0
    computer_score = 0

    # create fleet for the player
    players_fleet = enter_coordinates()
    print("Your fleet is ready! Check the map.")
    create_map(players_fleet)  # create map after all ships are placed

    # show ships filtered by size
    print("Big ship", big_ship)
    print("Medium ships", medium_ships)
    print("Small ships", small_ships)

    # fleet is created for pc
    computer_fleet = create_computer_fleet()
    print("Enemy fleet is ready.", computer_fleet)  # just checking if it works, delete before sending!

    # iteration of moves in guessing the opponent's ship location
    print("Yo Ho, Ho! Let's destroy some enemy ships!")
    players_moves(computer_fleet, players_fleet)


start_game = True
play_battleship(start_game)


# a function for playing game again util player ends it

# def start_new_game():
  #  """The main function for starting game"""
    # start_game = True
    # while start_game:
        #play_battleship(start_game)
        # ask_player = str(input("Do you want to play again? Y or N: "))
        # if ask_player == "y": return False
    # return True  ???





