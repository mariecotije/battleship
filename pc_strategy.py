import random

player_fleet = [(5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (5, 4), (6, 4), (7, 4), (2, 4), (2, 5), (2, 6), (0, 5), (1, 5),
                (2, 3), (3, 3), (0, 2), (1, 2)]

pc_missed_shots = []
pc_successful_shots = []

computer_score = 0


def pc_random_shot():
    pc_choice_column = random.randint(0, 9)
    pc_choice_row = random.randint(0, 9)
    pc_shot = (pc_choice_column, pc_choice_row)  # creating tuple from both random inputs

    return pc_shot


# pc_shot = pc_random_shot()


def pc_near_shot():
    last_successful_shot = pc_successful_shots[-1]
    print("Last hit:", last_successful_shot)
    (column, row) = last_successful_shot
    new_column = (column + 1)
    new_row = (row + 1)
    near_shot = (new_column, row)

    return near_shot


def decide_where_to():
    if pc_shot in pc_successful_shots:
        pc_near_shot()
    else:
        print("New random shot", pc_random_shot())


def check_pc_shot():

    print(f"Computer is sending missiles...")
    decide_where_to()

    if pc_shot in player_fleet:
        print(f"Damn! Enemy strike at {pc_shot} was successful!")
        player_fleet.remove(pc_shot)
        pc_successful_shots.append(pc_shot)

        # computer_score += 1
        # print("Computer score: ", computer_score)

        if len(player_fleet) == 0:
            print("Ay, caramba! Your fleet was destroyed!")  # computer destroyed all player's ships
    elif pc_shot not in player_fleet:
        print(f"Computer missed at {pc_shot}")
        pc_missed_shots.append(pc_shot)



for i in range(3):
    check_pc_shot()
    print("Missed: ", pc_missed_shots)
    print("Good: ", pc_successful_shots)
