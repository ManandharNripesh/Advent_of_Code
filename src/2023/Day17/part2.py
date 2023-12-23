from ...common.input_reader import read_input
import sys
import heapq

input_lines = read_input("src/2023/Day17/test.txt")

city = []

for i, input_line in enumerate(input_lines):
    city.append([int(input_space) for input_space in input_line.strip()])

dists = [[(sys.maxsize, ">", 0) for _ in range(len(city[0]))] for _ in range(len(city))]
dists[0][0] = (0, ">", 0)

def get_up(neighbors:list, dist:int, direction:str, steps:int, i:int, j:int):
    if i-1 >= 0:
        if direction == "^":
            if steps < 10:
                neighbors.append((dist + city[i-1][j], "^", steps+1, i-1, j))
        else:
            if steps == 0 or steps >= 4:
                neighbors.append((dist + city[i-1][j], "^", 1, i-1, j))

def get_down(neighbors:list, dist:int, direction:str, steps:int, i:int, j:int):
    if i+1 < len(city):
        if direction == "v":
            if steps < 10:
                neighbors.append((dist + city[i+1][j], "v", steps+1, i+1, j))
        else:
            if steps == 0 or steps >= 4:
                neighbors.append((dist + city[i+1][j], "v", 1, i+1, j))

def get_left(neighbors:list, dist:int, direction:str, steps:int, i:int, j:int):
    if j-1 >= 0:
        if direction == "<":
            if steps < 10:
                neighbors.append((dist + city[i][j-1], "<", steps+1, i, j-1))
        else:
            if steps == 0 or steps >= 4:
                neighbors.append((dist + city[i][j-1], "<", 1, i, j-1))

def get_right(neighbors:list, dist:int, direction:str, steps:int, i:int, j:int):
    if j+1 < len(city[0]):
        if direction == ">":
            if steps < 10:
                neighbors.append((dist + city[i][j+1], ">", steps+1, i, j+1))
        else:
            if steps == 0 or steps >= 4:
                neighbors.append((dist + city[i][j+1], ">", 1, i, j+1))

def get_neighbors(dist:int, direction:str, steps:int, i:int, j:int):
    neighbors = []
    match direction:
        case ">":
            get_up(neighbors, dist, direction, steps, i, j)
            get_right(neighbors, dist, direction, steps, i, j)
            get_down(neighbors, dist, direction, steps, i, j)
        case "<":
            get_up(neighbors, dist, direction, steps, i, j)
            get_left(neighbors, dist, direction, steps, i, j)
            get_down(neighbors, dist, direction, steps, i, j)
        case "^":
            get_left(neighbors, dist, direction, steps, i, j)
            get_up(neighbors, dist, direction, steps, i, j)
            get_right(neighbors, dist, direction, steps, i, j)
        case "v":
            get_left(neighbors, dist, direction, steps, i, j)
            get_down(neighbors, dist, direction, steps, i, j)
            get_right(neighbors, dist, direction, steps, i, j)
    return neighbors

cur_paths = [(dists[0][0][0], dists[0][0][1], dists[0][0][2], 0, 0)]
seen_directions_steps = [[[] for _ in range(len(city[0]))] for _ in range(len(city))]

while cur_paths:
    cur_path = heapq.heappop(cur_paths)
    dist, direction, steps, i, j = cur_path
    neighbors = get_neighbors(dist, direction, steps, i, j)
    for v in neighbors:
        dist_v, direction_v, steps_v, i_v, j_v = v
        if dist_v < dists[i_v][j_v][0]:
            dists[i_v][j_v] = (dist_v, direction_v, steps_v)
        if steps > 0:
            seen = False
            broken = False
            for seen_i, seen_directions_step in enumerate(seen_directions_steps[i_v][j_v]):
                if direction_v == seen_directions_step[0] and steps_v == seen_directions_step[1]:
                    seen = True
                    if dist_v > dists[i_v][j_v][0]:
                        broken = True
                        break
                    seen_directions_steps[i_v][j_v][seen_i] = (direction_v, steps_v, dist_v)
            if broken:
                continue
            if not seen:
                seen_directions_steps[i_v][j_v].append((direction_v, steps_v, dist_v))
        heapq.heappush(cur_paths, v)

print(dists[-1][-1][0])