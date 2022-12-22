from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day17/test.txt")

moves = ""
rocks = [
    [
        ['#', '#', '#', '#']
    ],
    [
        ['.', '#', '.'],
        ['#', '#', '#'],
        ['.', '#', '.']
    ],
    [
        ['.', '.', '#'],
        ['.', '.', '#'],
        ['#', '#', '#']
    ],
    [
        ['#'],
        ['#'],
        ['#'],
        ['#']
    ],
    [
        ['#', '#'],
        ['#', '#']
    ]
]

# make lower y correspond to lower pixels
for i, rock in enumerate(rocks):
    rocks[i].reverse()

for input_line in input_lines:
    input_line = input_line.strip()

    moves = input_line

num_rocks = 2022
max_width = 7
max_height = (num_rocks // 5 + 1) * 13 + 3

stack = [['.'] * max_width for _ in range(max_height)]

curr_height = 0
move_i = 0

for i in range(num_rocks):
    start_move_i = move_i
    rock_i = i
    rock = rocks[i % 5]
    rock_width = len(rock[0])
    rock_height = len(rock)

    x = 2

    for _ in range(3):
        # try to move left/right
        move = moves[move_i]
        move_i = (move_i + 1) % len(moves)
        if move == '>':
            if x + rock_width < max_width:
                x += 1
        else:
            if x > 0:
                x -= 1
    
    y = curr_height

    done = False

    # move down until can't
    while not done:
        # try to move left/right
        move = moves[move_i]
        move_i = (move_i + 1) % len(moves)
        if move == '>':
            if x + rock_width < max_width:
                horizontal_done = False
                for rock_y in range(rock_height):
                    for rock_x in range(rock_width):
                        if rock[rock_y][rock_x] == '#':
                            check_x = x + rock_x + 1
                            if stack[y + rock_y][check_x] != '.':
                                horizontal_done = True
                                break
                    if horizontal_done:
                        break
                if not horizontal_done:
                    x += 1
        else:
            if x > 0:
                horizontal_done = False
                for rock_y in range(rock_height):
                    for rock_x in range(rock_width):
                        if rock[rock_y][rock_x] == '#':
                            check_x = x + rock_x - 1
                            if stack[y + rock_y][check_x] != '.':
                                horizontal_done = True
                                break
                    if horizontal_done:
                        break
                if not horizontal_done:
                    x -= 1
        # try to move down
        for rock_y in range(rock_height):
            for rock_x in range(rock_width):
                if rock[rock_y][rock_x] == '#':
                    check_y = y + rock_y - 1
                    if check_y < 0 or stack[check_y][x + rock_x] != '.':
                        done = True
                        break
            if done:
                break
        if not done:
            y -= 1

    curr_height = max(curr_height, y + rock_height)
    for rock_y in range(rock_height):
        for rock_x in range(rock_width):
            if rock[rock_y][rock_x] == '#':
                stack[y + rock_y][x + rock_x] = '#'
    
for i in range(len(stack) - 1, -1, -1):
    row = "|"
    for rock in stack[i]:
        row += rock
    row += "|"
    print(row)
print("+-------+")

print(curr_height)
print(start_move_i, move_i, moves[start_move_i:move_i], rock_i, rocks[rock_i % 5])