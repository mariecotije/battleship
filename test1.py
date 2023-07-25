import random


def computer_ships():
    pc_big_ship = []
    pc_medium_ship = []
    pc_small_ship = []

    computer_ships = []
    ship_sizes = [5, 3, 3, 2, 2, 2]
    # create big ship
    while len(computer_ships) != 17:  # all ships coordinates
        ship_size = random.choice(ship_sizes)  # choose size from the list
        ship_sizes.remove(ship_size)  # remove chosen number from the list
        print("Chosen size: ", ship_size)
        print("Updated list: ", ship_sizes)

        for ship in range(ship_size):
            column = random.randint(0, 9)
            row = random.randint(0, 9)
            if ship_size == 5:
                pc_big_ship.append((column, row))
            elif ship_size == 3:
                pc_medium_ship.append((column, row))
            elif ship_size == 2:
                pc_small_ship.append((column, row))

            computer_ships = pc_small_ship + pc_medium_ship + pc_big_ship
            print("Big: ", pc_big_ship)
            print("Medium: ", pc_medium_ship)
            print("Small: ", computer_ships)
    return computer_ships


print(computer_ships())
