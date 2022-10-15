def read_input(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()

    return lines