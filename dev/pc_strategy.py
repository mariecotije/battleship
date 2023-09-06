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

def pc_next_column_forward():
    last_successful_shot = pc_successful_shots[-1]
    print("Last hit:", last_successful_shot)
    (column, row) = last_successful_shot
    new_column = (column + 1)
    next_column_forward_coordinates = (new_column, row)

    return next_column_forward_coordinates


def pc_next_row_down():
    last_successful_shot = pc_successful_shots[-1]
    print("Last hit:", last_successful_shot)
    (column, row) = last_successful_shot
    new_row = (row + 1)
    next_row_down_coordinates = (column, new_row)

    return next_row_down_coordinates


def pc_decide_where_to_send_missiles():
    if len(pc_successful_shots) == 0 and len(pc_missed_shots) == 0:
        pc_shot = pc_random_shot()
        print("PC made random shot")
    elif len(pc_successful_shots) == 0:
        pc_shot = pc_random_shot()
        print("PC made random shot after previous missed shot")
    else:
        pc_shot = pc_next_column_forward()
        print(f"PC made next column shot {pc_shot}")
        if pc_shot in pc_successful_shots or pc_shot in pc_missed_shots:
            print("Next column forward coordinates were already used")
            pc_shot = pc_next_row_down()
            print("PC made next row down shot")
            if pc_shot in pc_missed_shots:
                print("Next row coordinates were already used. New random shot.")
                pc_shot = pc_random_shot()

    return pc_shot


def check_pc_shot():

    print(f"Computer is sending missiles...")
    pc_shot = pc_decide_where_to_send_missiles()

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



for i in range(10):
    check_pc_shot()
    print("Missed: ", pc_missed_shots)
    print("Good: ", pc_successful_shots)
