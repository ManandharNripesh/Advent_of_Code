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

final_x = 0
final_y = 0
done = False

map_max = 4000000

points_to_check = set()

for i in range(len(dists)):
    s_x, s_y = s_points[i]
    b_x, b_y = b_points[i]
    dist = dists[i]

    for dy in range(-(dist+1), dist+2):
        if s_y + dy <= map_max and s_y + dy >= 0:
            dx = dist + 1 - abs(dy)
            if s_x + dx <= map_max and s_x + dx >= 0:
                points_to_check.add((s_x + dx, s_y + dy))
            if s_x - dx <= map_max and s_x - dx >= 0:
                points_to_check.add((s_x - dx, s_y + dy))

print(len(points_to_check))

count = 0

for point in points_to_check:
    count += 1
    if count % 1000000 == 0:
        print(count)
    x, y = point
    
    possible = True

    for i in range(len(dists)):
        s_x, s_y = s_points[i]
        dist = dists[i]

        dy = y - s_y
        dx = x - s_x
        if abs(dy) + abs(dx) <= dist:
            possible = False
            break
    
    if possible:
        final_x = x
        final_y = y


print(final_x * 4000000 + final_y)