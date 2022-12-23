from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day18/test.txt")

max_len = 0

for input_line in input_lines:
    input_line = input_line.strip()

    x, y, z = input_line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)

    max_len = max(max_len, x, y, z)

max_len += 1

cubes = [[[False for _ in range(max_len)] for _ in range(max_len)] for _ in range(max_len)]

for input_line in input_lines:
    input_line = input_line.strip()

    x, y, z = input_line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)

    cubes[x][y][z] = True

surface_area = 0
num_cubes = 0

for x in range(max_len):
    for y in range(max_len):
        for z in range(max_len):
            if cubes[x][y][z]:
                num_cubes += 1
                open_sides = 0
                
                if x == 0 or not cubes[x - 1][y][z]:
                    open_sides += 1
                if x == max_len - 1 or not cubes[x + 1][y][z]:
                    open_sides += 1
                if y == 0 or not cubes[x][y - 1][z]:
                    open_sides += 1
                if y == max_len - 1 or not cubes[x][y + 1][z]:
                    open_sides += 1
                if z == 0 or not cubes[x][y][z - 1]:
                    open_sides += 1
                if z == max_len - 1 or not cubes[x][y][z + 1]:
                    open_sides += 1

                surface_area += open_sides
            
print(surface_area)