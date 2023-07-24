import random


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


# create player fleet
def enter_coordinates():  # create any ship coordinates tuple

    # lists for verification of the amount of concrete types
    big_ship = []
    medium_ships = []
    small_ships = []

    ships = [2, 3, 5]  # list of ship sizes for verification of input ship_size

    min_allowed_value = 0
    max_allowed_value = 9

    fleet = []
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

        print("Fleet: ", fleet)  # show already saved coordinates

    return fleet


def create_computer_fleet():
    """A function that places computer ships using random method.
    If place is occupied, it tries again until fleet is completed"""

    computer_fleet = []
    for ship in range(2):  # same size of the fleet
        valid_position = False
        while not valid_position:
            column = random.randint(0, 9)
            row = random.randint(0, 9)
            if (column, row) not in computer_fleet:
                computer_fleet.append((column, row))  # adding a coordinates tuple to the list
                valid_position = True

    return computer_fleet


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

    # messages to show when player hith the enemy ship
    messages = [
        "You missed",
        "Impressive shot, but missed",
        "No enemy ships there"
    ]

    # main iteration loop
    while computer_fleet != 0 and player_fleet != 0:
        try:
            player_input = input("Enter two space separated numbers 0-9 and press Enter: ")  # user  input
            coordinates = tuple(int(number) for number in player_input.split())  # converting user input to tuple
            if len(coordinates) < 2 or len(coordinates) > 2:  # prevent sending user input if not 2 coordinates
                print("Two coordinates are needed for shot. Try again.")
                continue
        except ValueError:  # prevent app from failing when user inserts non integer
            print("Please enter 2 space separated numbers in range 0-9.")
            continue
        else:
            if coordinates in computer_fleet:
                print("Nice shot! A ship was hit!")
                computer_fleet.remove(coordinates)
                player_score += 1
                print("Your score: ", player_score)
                print("Enemy fleet status: ", len(computer_fleet))  # showing player the count of ships remained
                if len(computer_fleet) == 0:
                    print("Congratulations! You sunk all the computer's ships! GAME OVER")
                    break
            elif coordinates not in computer_fleet:
                print(coordinates)
                print(random.choice(messages))  # show a random message form the list
                print("PC remain: ", computer_fleet)  # delete before sending
                # check the ship was destroyed and remove from list of coordinates

        # computer turn
        pc_choice_column = random.randint(0, 1)
        pc_choice_row = random.randint(0, 1)
        pc_shot = (pc_choice_column, pc_choice_row)  # creating tuple from both random inputs
        print(f"Computer is sending missiles...")
        if pc_shot in player_fleet:
            print(f"Damn! Your ship at {pc_shot} was hit!")
            player_fleet.remove(pc_shot)
            print("Your fleet status: ", len(player_fleet))  # count of ships remained in the fleet
            computer_score += 1
            print("Enemy's score: ", computer_score)
            if len(player_fleet) == 0:
                print("Ay, caramba! Your fleet was destroyed!")
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {pc_shot}")


def play_battleship(start_game):
    """a main function where the player and computer iterate in guessing the opponent's ship location"""

    # welcome message
    print("Ahoy Captain! Let's create your fleet!")

    # initial score for both players
    player_score = 0
    computer_score = 0

    # create fleet for the player
    player_fleet = enter_coordinates()
    create_map(player_fleet)  # create map after all ships are placed
    print("Your fleet is ready: ", player_fleet)

    # fleet is created for pc
    computer_fleet = create_computer_fleet()
    print("Enemy fleet is ready: ", computer_fleet)  # just checking if it works, delete before sending!

    # iteration of moves in guessing the opponent's ship location
    print("Let's destroy some enemy ships!")
    players_moves(computer_fleet, player_fleet)


start_game = True
play_battleship(start_game)

# def play_game():
  #  """A main function for playing game"""




