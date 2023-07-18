import random


# sample steps

# Write a function that creates a grid (map) where ships will be placed. The function
# should take a list of coordinate pairs as an input, which represents the position of the
# ship. The grid should be 10 spaces by 10 spaces big and for simplicity at the
# beginning consider ships only one space big.

def create_map(ship_coordinates):
    grid = [['.' for _ in range(10)] for _ in range(10)]  # Create a 10x10 grid filled with dots

    for coordinate in ship_coordinates:
        x, y = coordinate
        if 0 <= x < 10 and 0 <= y < 10:  # Check if the coordinate is within the grid boundaries
            grid[y][x] = 'X'  # Place the ship at the specified coordinate

    # Print the map using nested for loops
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()


# Create a function that allows the user to select positions for their ships. Store this in
# a format that your draw function from Step 1 can accept as an argument. Limit the
# number of ships and verify that a position is not already taken or not outside of a
# map. After the user selects their ships, draw a map using the function from point 1.

def create_player_fleet(fleet):
    """a function that allows the user to select positions for their ships"""

    ship_coordinates = []
    for ship in range(3):
        valid_position = False
        while not valid_position:  # ask player to enter coordinates until there is enough amount of ships in the fleet
            coordinate = input(f"Ahoy Captain! Enter the coordinates for ship {ship + 1} (x, y): ")
            try:
                x, y = map(int, coordinate.split(','))
                if 0 <= x < 10 and 0 <= y < 10:  # Check if the coordinate is within the grid boundaries
                    if (x, y) not in ship_coordinates:  # Check if the position is already taken
                        ship_coordinates.append((x, y))
                        valid_position = True
                    else:
                        print("Position already taken. Please select a different position.")
                else:
                    print("Position is out of the filed. Please enter values between 0 and 9.")
            except ValueError:
                print("Invalid input format. Please enter coordinates in the format 'x, y'.")

    return ship_coordinates


# Create a function that randomly places computer ships (also check that nothing
# exists on target position), but does not display the board to the player.

def create_computer_fleet(fleet):
    """a function that randomly places computer ships"""

    pc_ship_coordinates = []
    for ship in range(fleet):
        valid_position = False
        while not valid_position:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in pc_ship_coordinates:
                pc_ship_coordinates.append((x, y))
                valid_position = True

    return pc_ship_coordinates


# Write a function where after asking for input, you check if the opponent's ship was
# destroyed. If yes, remove the ship from the list of coordinates. create either two
# functions (one for the player, second for the computer) or try setting default
# arguments to a single function to play randomly for the computer.


def player_move(computer_fleet):
    """a function that checks the ship status after player's move"""

    player_move = input("Enter enemy ship coordinates: ")
    try:
        x, y = map(int, player_move.split(','))
        if 0 <= x < 10 and 0 <= y < 10:
            if (x, y) in computer_fleet:
                print("Nice hit! Enemy ship was destroyed!")
                computer_fleet.remove((x, y))
            else:
                print("Oops! You missed.")
        else:
            print("Invalid coordinates. Please enter values between 0 and 9.")
    except ValueError:
        print("Invalid input format. Please enter coordinates in the format 'x, y'.")


def computer_move(player_fleet):
    """a function that checks the ship status after pc move"""

    pc_move = random.choice(player_fleet)
    print(f"The computer sent a missile to: {pc_move[0]}, {pc_move[1]}")
    if pc_move in player_fleet:
        print("The computer hit your ship!")
        player_fleet.remove(pc_move)
    else:
        print("The computer missed your ship.")


# Let's put it together: write a main function where the player and computer (after
# placing their ships) iterate in guessing the opponent's ship location. Keep score and
# let players know their successes or misses. The game ends when one of the player's
# lists of ships is empty. Congratulations! You have a game!


def play_battleship(start_game):
    """a main function where the player and computer iterate in guessing the opponent's ship location"""

    # number of ships is reduced for testing, change back after finishing

    # the player and computer are placing their ships
    fleet = 2
    player_fleet = create_player_fleet(fleet)
    create_map(player_fleet)
    computer_fleet = create_computer_fleet(fleet)
    print(computer_fleet)

    # iteration of moves in guessing the opponent's ship location


    # Keep score and let players know their successes or misses

    # game status
    if len(player_fleet) == 0:
        print("Ay, caramba! Your fleet was destroyed!")
    else:
        print("Congratulations! You sunk all the computer's ships!")


start_game = True
play_battleship(start_game)
