def convert_pc_coordinates(pc_tuple_coordinates):
    (column, row) = pc_tuple_coordinates

    match column:
        case 0:
            column = "A"
        case 1:
            column = "B"
        case 2:
            column = "C"
        case 3:
            column = "D"
        case 4:
            column = "E"
        case 5:
            column = "F"
        case 6:
            column = "G"
        case 7:
            column = "H"
        case 8:
            column = "I"
        case 9:
            column = "J"

    converted_pc_coordinates = (column, (row + 1))

    return converted_pc_coordinates


pc_shot = (9, 9)
print(convert_pc_coordinates(pc_shot))
