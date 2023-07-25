if len(big_ship) == 5:
    continue
elif len(medium_ship) == 6:
    continue
elif len(small_ship) == 6:
    continue

    if len(ship) == 5:
        big_ship.extend(ship)
        print("Big: ", big_ship)
    elif len(ship) == 3:
        medium_ship.extend(ship)
        print("Medium: ", medium_ship)
    elif len(ship) == 2:
        small_ship.extend(ship)
        print("Small: ", small_ship)

    fleet = big_ship + medium_ship + small_ship
    print(len(fleet))
