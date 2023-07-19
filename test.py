# Write a function where after asking for input, you check if the opponent's ship was
# destroyed. If yes, remove the ship from the list of coordinates. create either two
# functions (one for the player, second for the computer) or try setting default
# arguments to a single function to play randomly for the computer.

import random


def players_moves(computer_fleet, player_fleet):

    print("Let's destroy some enemy ships!")

    while computer_fleet != 0 and player_fleet != 0:
        player_input = input('Enter space separated coordinates: ')  # user  input
        coordinates = tuple(int(item) for item in player_input.split())  # converting user input to tuple
        # check the ship was destroyed and remove from list of coordinates
        if coordinates in computer_fleet:
            print("Nice shot! A ship was destroyed!")
            computer_fleet.remove(coordinates)
        elif coordinates not in computer_fleet:
            print("Missed! Don't worry, you will have another shot!")
        # pc input
        pc_choice_row = random.randint(0, 9)
        pc_choice_cell = random.randint(0, 9)
        pc_shot = (pc_choice_row, pc_choice_cell)  # creating tuple
        print(f"Computer is sending missiles...")
        if pc_shot in player_fleet:
            print(f"Damn! Your ship at {pc_shot} was destroyed!")
            computer_fleet.remove(pc_shot)
        elif pc_shot not in player_fleet:
            print(f"Computer missed at {pc_shot}")


player_fleet = [(1, 0), (1, 1)]
computer_fleet = [(0, 2), (5, 9)]
players_moves(computer_fleet, player_fleet)
print(computer_fleet)
