import random

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
            print("Enemy fleet counts: ", len(computer_fleet))  # letting player know how many ships remained to destroy
            if len(computer_fleet) == 0:
                print("Congratulations! You sunk all the computer's ships! GAME OVER")
                break
        elif coordinates not in computer_fleet:
            print(coordinates)
            print("Missed! Don't worry, you will have another shot! PC remain: ", computer_fleet)  # delete before sending
        # pc input
        pc_choice_column = random.randint(0, 1)
        pc_choice_row = random.randint(0, 1)
        pc_shot = (pc_choice_column, pc_choice_row)  # creating tuple from both random inputs
        print(f"Computer is sending missiles...")
        if pc_shot in player_fleet:
            print(f"Damn! Your ship at {pc_shot} was destroyed!")
            player_fleet.remove(pc_shot)
            print("Ships remained in your fleet: ", len(player_fleet))  # count of ships remained in the fleet
            if len(player_fleet) == 0:
                print("Ay, caramba! Your fleet was destroyed!")
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {pc_shot}")
            