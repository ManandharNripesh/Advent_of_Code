from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day10/test.txt")

pipe_map = []
start_pos = (-1,-1)


for i, input_line in enumerate(input_lines):
    pipe_map.append(input_line)

    if "S" in input_line:
        start_pos = (i, input_line.index("S"))

positions = []
dirs = []

for offset in range(-1, 2, 2):
    # check vertically
    i = start_pos[0] + offset
    j = start_pos[1]

    if i >= 0 and i < len(pipe_map):
        if offset < 0:
            if pipe_map[i][j] in "|7F":
                positions.append((i, j))
                dirs.append("N")
        else: #elif offset > 0:
            if pipe_map[i][j] in "|LJ":
                positions.append((i, j))
                dirs.append("S")
    
    # check horizontally
    i = start_pos[0]
    j = start_pos[1] + offset

    if j >= 0 and j < len(pipe_map[0]):
        if offset < 0:
            if pipe_map[i][j] in "-LF":
                positions.append((i, j))
                dirs.append("W")
        else: #elif offset > 0:
            if pipe_map[i][j] in "-J7":
                positions.append((i, j))
                dirs.append("E")

dir_counts = {
    "N": 0,
    "E": 0,
    "W": 0,
    "S": 0
}

for cur_dir in dirs:
    dir_counts[cur_dir] += 1

i, j = start_pos
if dir_counts["N"] > 0:
    if dir_counts["S"] > 0:
        pipe_map[i] = pipe_map[i][:j] + "|" + pipe_map[i][j+1:]
    elif dir_counts["E"] > 0:
        pipe_map[i][j] = pipe_map[i][:j] + "L" + pipe_map[i][j+1:]
    elif dir_counts["W"] > 0:
        pipe_map[i][j] = pipe_map[i][:j] + "J" + pipe_map[i][j+1:]
elif dir_counts["S"] > 0:
    if dir_counts["E"] > 0:
        pipe_map[i][j] = pipe_map[i][:j] + "F" + pipe_map[i][j+1:]
    elif dir_counts["W"] > 0:
        pipe_map[i][j] = pipe_map[i][:j] + "7" + pipe_map[i][j+1:]
elif dir_counts["E"] > 0:
    if dir_counts["W"] > 0:
        pipe_map[i][j] = pipe_map[i][:j] + "-" + pipe_map[i][j+1:]

# first mark which tiles are part of the loop

loop_tiles = ["." * len(pipe_map[0]) for _ in pipe_map]

i, j = start_pos
loop_tiles[i] = loop_tiles[i][:j] + "P" + loop_tiles[i][j+1:]

for pos_num in range(len(positions)):
    i, j = positions[pos_num]
    loop_tiles[i] = loop_tiles[i][:j] + "P" + loop_tiles[i][j+1:]

while positions[0] != positions[1]:
    next_positions = positions.copy()
    next_dirs = dirs.copy()

    for pos_num in range(len(positions)):
        i, j = positions[pos_num]
        match pipe_map[i][j]:
            case "|":
                match dirs[pos_num]:
                    case "N":
                        next_positions[pos_num] = (i-1, j)
                    case "S":
                        next_positions[pos_num] = (i+1, j)
            case "-":
                match dirs[pos_num]:
                    case "W":
                        next_positions[pos_num] = (i, j-1)
                    case "E":
                        next_positions[pos_num] = (i, j+1)
            case "L":
                match dirs[pos_num]:
                    case "W":
                        next_positions[pos_num] = (i-1, j)
                        next_dirs[pos_num] = "N"
                    case "S":
                        next_positions[pos_num] = (i, j+1)
                        next_dirs[pos_num] = "E"
            case "J":
                match dirs[pos_num]:
                    case "E":
                        next_positions[pos_num] = (i-1, j)
                        next_dirs[pos_num] = "N"
                    case "S":
                        next_positions[pos_num] = (i, j-1)
                        next_dirs[pos_num] = "W"
            case "7":
                match dirs[pos_num]:
                    case "E":
                        next_positions[pos_num] = (i+1, j)
                        next_dirs[pos_num] = "S"
                    case "N":
                        next_positions[pos_num] = (i, j-1)
                        next_dirs[pos_num] = "W"
            case "F":
                match dirs[pos_num]:
                    case "W":
                        next_positions[pos_num] = (i+1, j)
                        next_dirs[pos_num] = "S"
                    case "N":
                        next_positions[pos_num] = (i, j+1)
                        next_dirs[pos_num] = "E"
    
    if positions[0] == next_positions[1]:
        break
    positions = next_positions.copy()
    dirs = next_dirs.copy()
    for pos_num in range(len(positions)):
        i, j = positions[pos_num]
        loop_tiles[i] = loop_tiles[i][:j] + "P" + loop_tiles[i][j+1:]

# remove non-loop tiles
for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if loop_tiles[i][j] == ".":
            pipe_map[i] = pipe_map[i][:j] + "." + pipe_map[i][j+1:]

# count inside tiles
inside_count = 0
for i, row in enumerate(pipe_map):
    j = 0
    inside = False
    while j < len(row):
        match row[j]:
            case "|":
                inside = not inside
            case "L":
                while row[j] not in "J7":
                    j += 1
                if row[j] == "7":
                    inside = not inside
            case "F":
                while row[j] not in "J7":
                    j += 1
                if row[j] == "J":
                    inside = not inside
            case ".":
                if inside:
                    pipe_map[i] = pipe_map[i][:j] + "I" + pipe_map[i][j+1:]
                    inside_count += 1
        j += 1

print(inside_count)