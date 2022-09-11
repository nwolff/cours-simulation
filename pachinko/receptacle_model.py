def new_receptacle(size):
    return [0 for _ in range(size)]


def add_to_bucket(receptacle, index):
    receptacle[index] += 1
    return receptacle[index]
