import random


# sample steps

# Write a function that creates a grid (map) where ships will be placed. The function
# should take a list of coordinate pairs as an input, which represents the position of the
# ship. The grid should be 10 spaces by 10 spaces big and for simplicity at the
# beginning consider ships only one space big.

def create_ship_field(ship_coordinates):
    grid = [['.' for _ in range(10)] for _ in range(10)]  # Create a 10x10 grid filled with dots

    for coordinate in ship_coordinates:
        x, y = coordinate
        if 0 <= x < 10 and 0 <= y < 10:  # Check if the coordinate is within the grid boundaries
            grid[y][x] = 'X'  # Place the ship at the specified coordinate

    # Print the grid using nested for loops
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()


player_fleet = [(1, 2), (4, 7), (9, 5)]
create_ship_field(player_fleet)


# Create a function that allows the user to select positions for their ships. Store this in
# a format that your draw function from Step 1 can accept as an argument. Limit the
# number of ships and verify that a position is not already taken or not outside of a
# map. After the user selects their ships, draw a map using the function from point 1.

def select_positions(coordinates):
    """a function that allows the user to select positions for their ships"""

    ship_coordinates = []
    for ship in range(fleet):
        valid_position = False
        while not valid_position:
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


# number of ships is reduced for testing, change back after finishing
fleet = 2
player_fleet = select_positions(fleet)
create_ship_field(player_fleet)


# Create a function that randomly places computer ships (also check that nothing
# exists on target position), but does not display the board to the player.

def computer_ships_positions(fleet):
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


fleet = 3
computer_ship_field = computer_ships_positions(fleet)
print(computer_ship_field)

# Write a function where after asking for input, you check if the opponent's ship was
# destroyed. If yes, remove the ship from the list of coordinates. create either two
# functions (one for the player, second for the computer) or try setting default
# arguments to a single function to play randomly for the computer.


def player_move(computer_ship_field):
    """a function that checks the ship status after player's move"""

    move = input("Enter enemy ship coordinates: ")
    try:
        x, y = map(int, move.split(','))
        if 0 <= x < 10 and 0 <= y < 10:
            if (x, y) in computer_ship_field:
                print("Congratulations! You hit the opponent's ship!")
                computer_ship_field.remove((x, y))
            else:
                print("Oops! You missed the opponent's ship.")
        else:
            print("Invalid coordinates. Please enter values between 0 and 9.")
    except ValueError:
        print("Invalid input format. Please enter coordinates in the format 'x, y'.")


def computer_move(player_fleet):
    """a function that checks the ship status after pc move"""

    pc_move = random.choice(player_fleet)
    print(f"The computer selected target: {pc_move[0]}, {pc_move[1]}")
    if pc_move in player_fleet:
        print("The computer hit your ship!")
        player_fleet.remove(pc_move)
    else:
        print("The computer missed your ship.")



# Let's put it together: write a main function where the player and computer (after
# placing their ships) iterate in guessing the opponent's ship location. Keep score and
# let players know their successes or misses. The game ends when one of the player's
# lists of ships is empty. Congratulations! You have a game!


def play_battleship():
    """a main function where the player and computer iterate in guessing the opponent's ship location"""

def play_battleship(player_mode):
    num_ships = 3
    player_ship_coords = select_ship_positions(num_ships)
    computer_ship_coords = randomly_place_computer_ships(num_ships)

    while len(player_ship_coords) > 0 and len(computer_ship_coords) > 0:
        if player_mode:
            print("Player's Turn:")
            player_turn(computer_ship_coords)
            print()
        else:
            print("Computer's Turn:")
            computer_turn(player_ship_coords)
            print()

    if len(player_ship_coords) == 0:
        print("Game Over! The computer wins!")
    else:
        print("Congratulations! You sunk all the computer's ships!")