import random


def first_coordinates():

    column = random.randint(0, 9)
    row = random.randint(0, 9)

    return column, row


start_coordinates = first_coordinates()
print(start_coordinates)

# unpack tuple
(column, row) = start_coordinates
print(column)
print(row)
