import random


def create_map(ship_coordinates):
    """A function that takes as an argument list of player's ship coordinates and prints a map with X as ship mark"""
    grid = [['.' for _ in range(10)] for _ in range(10)]  # Create a 10x10 grid filled with dots

    for coordinate in ship_coordinates:
        row, cell = coordinate
        if 0 <= row < 10 and 0 <= cell < 10:  # Check if the coordinate is within the grid boundaries
            grid[cell][row] = 'X'  # Place the ship at the specified coordinate

    # Print the map using nested for loops
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()


def create_player_fleet():
    """A function that asks player for ship coordinates one by one and returns a list of all ships coordinates.
    The list is used for map"""

    ship_coordinates = []
    num_ships = 0  # total number of ships in the fleet

    while num_ships < 2:  # Size of the fleet
        print(f"Select position for Ship {num_ships + 1}")
        input_coordinates = input('Enter two space separated numbers (0-9): ')  # user  input
        coordinates = tuple(int(item) for item in input_coordinates.split())  # converting user input to tuple

        #if input_coordinates < 0 or input_coordinates > 9 or input_coordinates < 0 or input_coordinates > 9:
            #print("Invalid position. Try again.")
            #continue

        if coordinates in ship_coordinates:
            print("Position already taken. Try again.")
            continue

        ship_coordinates.append(coordinates)  # adding a coordinates tuple to the list
        num_ships += 1

    return ship_coordinates


def create_computer_fleet():
    """A function that places computer ships using random method.
    If place is occupied, it tries again until fleet is completed"""

    computer_fleet = []
    for ship in range(2):  # same size of the fleet
        valid_position = False
        while not valid_position:
            row = random.randint(0, 9)
            cell = random.randint(0, 9)
            if (row, cell) not in computer_fleet:
                computer_fleet.append((row, cell))  # adding a coordinates tuple to the list
                valid_position = True

    return computer_fleet


def players_moves(computer_fleet, player_fleet):
    """A function for main iteration between players.
    User is making first move by inserting 2 numbers separated by space. Input is converted to tuple.
    If the tuple is in the list of the user's fleet, the ship is destroyed and the tuple is removed from the list.
    Next move is for computer.
    Computer input is generated tuple from 2 random integers. The same logic for destroyed ship.
    Iteration continues until one of the fleets is destroyed completely, means the list is empty."""

    while computer_fleet != 0 and player_fleet != 0:
        player_input = input('Enter space separated coordinates: ')  # user  input
        coordinates = tuple(int(item) for item in player_input.split())  # converting user input to tuple
        # check the ship was destroyed and remove from list of coordinates
        if coordinates in computer_fleet:
            print("Nice shot! A ship was destroyed!")
            computer_fleet.remove(coordinates)
            print("Enemy fleet counts: ", len(computer_fleet))
            if len(computer_fleet) == 0:
                print("Congratulations! You sunk all the computer's ships! GAME OVER")
                break
        elif coordinates not in computer_fleet:
            print(coordinates)
            print("Missed! Don't worry, you will have another shot! PC remain: ", computer_fleet)
        # pc input
        pc_choice_row = random.randint(0, 1)
        pc_choice_cell = random.randint(0, 1)
        pc_shot = (pc_choice_row, pc_choice_cell)  # creating tuple from both random inputs
        print(f"Computer is sending missiles...")
        if pc_shot in player_fleet:
            print(f"Damn! Your ship at {pc_shot} was destroyed!")
            player_fleet.remove(pc_shot)
            print("Ships remained in your fleet: ", len(player_fleet))
            if len(player_fleet) == 0:
                print("Ay, caramba! Your fleet was destroyed!")
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {pc_shot}")


def play_battleship(start_game):
    """a main function where the player and computer iterate in guessing the opponent's ship location"""
    # welcome message
    print("Ahoy Captain! Let's create your fleet!")

    # initial score for both players
    user_score = 0
    computer_score = 0

    # create fleet for the player
    player_fleet = create_player_fleet()
    create_map(player_fleet)  # create map after all ships are placed
    print("Your fleet: ", player_fleet)

    # fleet is created for pc
    computer_fleet = create_computer_fleet()
    print("computer: ", computer_fleet)  # just checking if it works, delete before sending!

    # iteration of moves in guessing the opponent's ship location
    print("Let's destroy some enemy ships!")

    players_moves(computer_fleet, player_fleet)


start_game = True
play_battleship(start_game)
