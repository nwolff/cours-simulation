import random


def top_coord(height):
    return 0, height


def left_child(coord):
    x, y = coord
    return x, y - 1


def right_child(coord):
    x, y = coord
    return x + 1, y - 1


def is_at_bottom(coord):
    _, y = coord
    return y <= 0


def random_step(coord):
    choice = random.choice(("L", "R"))
    if choice == "L":
        return left_child(coord)
    else:
        return right_child(coord)


def simulate(height):
    """Returns a trail of coordinates"""
    coord = top_coord(height)
    result = []
    while not is_at_bottom(coord):
        new_coord = random_step(coord)
        result.append(new_coord)
        coord = new_coord
    return result
