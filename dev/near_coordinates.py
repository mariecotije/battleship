pc_fleet = [(5, 5)]
ship_coordinates_true = [(5, 5)]
ship_coordinates_false = [(0, 0)]
near_coordinates = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def create_near_ship_coordinates(ship_coordinates):
    new_near_coordinates = []
    for coordinates in ship_coordinates:
        (column, row) = coordinates
        for close_coordinates in near_coordinates:
            (near_column, near_row) = close_coordinates
            new_near_coordinates.append(((column + near_column), (row + near_row)))

    return new_near_coordinates


def position_is_occupied(ship_coordinates):
    """A function that checks coordinates in the whole fleet and returns response"""
    near_ship_coordinates = create_near_ship_coordinates(ship_coordinates)
    for near_coordinate_tuple in near_ship_coordinates:
        if near_coordinate_tuple in pc_fleet:
            return True

    return False


print(position_is_occupied(ship_coordinates_true))
print(create_near_ship_coordinates(ship_coordinates_false))
