import random


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
        "No ships at that point"
    ]

    # main iteration loop
    while computer_fleet != 0 and player_fleet != 0:
        try:
            player_input = input("Enter two space separated numbers 0-9 and press Enter: ")  # user  input
            coordinates = tuple(int(number) for number in player_input.split())  # converting user input to tuple
            if len(coordinates) < 2:  # prevent sending user input if not 2 coordinates
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
            print(("PC score: ", computer_score))
            if len(player_fleet) == 0:
                print("Ay, caramba! Your fleet was destroyed!")
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {pc_shot}")
