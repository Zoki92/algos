UP = "up"
RIGHT = "right"
LEFT = "left"
DOWN = "down"

def rectangleMania(coords):
    coords_table = get_coords_table(coords)
    return get_rectangle_count(coords, coords_table)

def get_rectangle_count(coords, coords_table):
    rectangle_count = 0
    for coord in coords:
        rectangle_count += clockwise_count_rectangles(coord, coords_table, UP, coord)
    return rectangle_count

def clockwise_count_rectangles(coord, coords_table, direction, origin):
    coord_string = coord_to_string(coord)
    if direction == LEFT:
        rectangle_found = origin in coords_table[coord_string][LEFT]
        return 1 if rectangle_found else 0
    else:
        rectangle_count = 0
        next_direction = get_next_clockwise_direction(direction)
        for next_coord in coords_table[coord_string][direction]:
            rectangle_count += clockwise_count_rectangles(next_coord, coords_table, next_direction, origin)
        return rectangle_count

def get_next_clockwise_direction(direction):
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    return ""

def get_coords_table(coords):
    coords_table = {}
    for coord1 in coords:
        coord1_directions = {UP: [], RIGHT: [], DOWN: [], LEFT: []}
        for coord2 in coords:
            coord2_direction = get_coord_direction(coord1, coord2)
            if coord2_direction in coord1_directions:
                coord1_directions[coord2_direction].append(coord2)
        coord1_string = coord_to_string(coord1)
        coords_table[coord1_string] = coord1_directions
    return coords_table

def get_coord_direction(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    if y2 == y1:
        if x2 > x1:
            return RIGHT
        elif x2 < x1:
            return LEFT
    elif x2 == x1:
        if y2 > y1:
            return UP
        elif y2 < y1:
            return DOWN
    return ""

def coord_to_string(coord):
    x, y = coord
    return f"{x}-{y}"


coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]

print(rectangleMania(coords))