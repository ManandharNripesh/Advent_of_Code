from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day15/test.txt")

s_points = []
b_points = []
dists = []

min_x = 0
max_x = 0
min_y = 0
max_y = 0

for input_line in input_lines:
    input_line = input_line.strip()

    words = input_line.split()

    s_x = int(words[2][2:-1])
    s_y = int(words[3][2:-1])
    s_points.append((s_x, s_y))

    b_x = int(words[8][2:-1])
    b_y = int(words[9][2:])
    b_points.append((b_x, b_y))

    dist = abs(s_x - b_x) + abs(s_y - b_y)
    dists.append(dist)

    min_x = min(s_x - dist, min_x)
    max_x = max(s_x + dist, max_x)
    min_y = min(s_y - dist, min_y)
    max_y = max(s_y + dist, max_y)

map_width = max_x - min_x + 1
map_height = max_y - min_y + 1

row = ['.'] * map_width

y_final = 2000000
final_row = ['.'] * map_width

for i in range(len(dists)):
    s_x, s_y = s_points[i]
    b_x, b_y = b_points[i]
    dist = dists[i]

    if s_y == y_final:
        row[s_x - min_x] = 'S'
    if b_y == y_final:
        row[b_x - min_x] = 'B'

    dy = y_final - s_y
    if abs(dy) <= dist:
        dx_lim = dist - abs(dy)
        left = s_x - dx_lim - min_x
        right = s_x + dx_lim + 1 - min_x
        final_row[left:right] = ["#"] * (right - left)

for i, pos in enumerate(row):
    if pos == "." and final_row[i] == "#":
        row[i] = "#"

count = 0
for pos in row:
    if pos == '#':
        count += 1

print(count)