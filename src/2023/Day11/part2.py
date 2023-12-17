from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day11/test.txt")

image = []
times_larger = 1000000 - 1

empty_rows = []
empty_cols = []

for i, input_line in enumerate(input_lines):
    row = input_line.strip()
    image.append(row)
    
    empty_row = True
    for space in row:
        if space != ".":
            empty_row = False
            break
    
    if empty_row:
        empty_rows.append(i)

j = 0
while j < len(image[0]):
    empty_col = True
    for i in range(len(image)):
        if image[i][j] != ".":
            empty_col = False
    if empty_col:
        empty_cols.append(j)
    j += 1

galaxy_positions = []

for i, row in enumerate(image):
    for j, space in enumerate(row):
        if space == "#":
            galaxy_positions.append((i, j))

def manhattan_dist(gp1, gp2):
    dist = abs(gp2[0] - gp1[0]) + abs(gp2[1] - gp1[1])

    start = min(gp1[0], gp2[0])
    stop = max(gp1[0], gp2[0])
    for i in range(start+1, stop):
        if i in empty_rows:
            dist += times_larger

    start = min(gp1[1], gp2[1])
    stop = max(gp1[1], gp2[1])
    for i in range(start+1, stop):
        if i in empty_cols:
            dist += times_larger

    return dist

dists = []

for gpi1, gp1 in enumerate(galaxy_positions):
    dists.append([])
    for gpi2, gp2 in enumerate(galaxy_positions):
        if gpi1 != gpi2:
            dists[gpi1].append(manhattan_dist(gp1, gp2))

sum_dist_list = [sum(dist_list) for dist_list in dists]

print(sum(sum_dist_list) // 2)