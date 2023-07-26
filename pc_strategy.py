import random


pc_sent_shots = []


def pc_sending_missiles():

    while len(pc_sent_shots) != 10:
        pc_choice_column = random.randint(0, 9)
        pc_choice_row = random.randint(0, 9)
        pc_shot = (pc_choice_column, pc_choice_row)
        pc_sent_shots.append(pc_shot)
        if pc_shot in pc_sent_shots:
            continue

    return pc_sent_shots


pc_sending_missiles()
print(pc_sent_shots)

