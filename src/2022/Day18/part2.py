from ...common.input_reader import read_input

import sys

sys.setrecursionlimit(300000)

input_lines = read_input("src/2022/Day18/test.txt")

max_len = 0

for input_line in input_lines:
    input_line = input_line.strip()

    x, y, z = input_line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)

    max_len = max(max_len, x, y, z)

max_len += 1 + 2

cubes = [[[False for _ in range(max_len)] for _ in range(max_len)] for _ in range(max_len)]

for input_line in input_lines:
    input_line = input_line.strip()

    x, y, z = input_line.split(",")
    x = int(x) + 1
    y = int(y) + 1
    z = int(z) + 1

    cubes[x][y][z] = True

surface_area = 0

checked = [[[False for _ in range(max_len)] for _ in range(max_len)] for _ in range(max_len)]

def expand(x, y, z):
    global surface_area
    
    # consider this cube
    checked[x][y][z] = True
    
    if cubes[x][y][z]:
        return

    closed_sides = 0

    if x > 0 and cubes[x-1][y][z]:
        closed_sides += 1
    if x < max_len-1 and cubes[x+1][y][z]:
        closed_sides += 1
    if y > 0 and cubes[x][y-1][z]:
        closed_sides += 1
    if y < max_len-1 and cubes[x][y+1][z]:
        closed_sides += 1
    if z > 0 and cubes[x][y][z-1]:
        closed_sides += 1
    if z < max_len-1 and cubes[x][y][z+1]:
        closed_sides += 1

    surface_area += closed_sides

    # consider next options
    options = []

    if x > 0:
        options.append((x-1, y, z))
    if x < max_len-1:
        options.append((x+1, y, z))
    if y > 0:
        options.append((x, y-1, z))
    if y < max_len-1:
        options.append((x, y+1, z))
    if z > 0:
        options.append((x, y, z-1))
    if z < max_len-1:
        options.append((x, y, z+1))

    for option in options:
        next_x, next_y, next_z = option
        if not checked[next_x][next_y][next_z]:
            expand(next_x, next_y, next_z)

for i in range(max_len):
    # variable x
    if not checked[i][0][0]:
        expand(i, 0, 0)
    if not checked[i][max_len-1][0]:
        expand(i, max_len-1, 0)
    if not checked[i][0][max_len-1]:
        expand(i, 0, max_len-1)
    if not checked[i][max_len-1][max_len-1]:
        expand(i, max_len-1, max_len-1)
    # variable y
    if not checked[0][i][0]:
        expand(0, i, 0)
    if not checked[max_len-1][i][0]:
        expand(max_len-1, i, 0)
    if not checked[0][i][max_len-1]:
        expand(0, i, max_len-1)
    if not checked[max_len-1][i][max_len-1]:
        expand(max_len-1, i, max_len-1)
    # variable z
    if not checked[0][0][i]:
        expand(0, 0, i)
    if not checked[max_len-1][0][i]:
        expand(max_len-1, 0, i)
    if not checked[0][max_len-1][i]:
        expand(0, max_len-1, i)
    if not checked[max_len-1][max_len-1][i]:
        expand(max_len-1, max_len-1, i)

print(surface_area)