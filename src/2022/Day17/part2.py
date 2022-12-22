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

rocks_left_indices = [
    [
        (0,0)
    ],
    [
        (1,2),
        (0,1),
        (1,0)
    ],
    [
        (2,2),
        (2,1),
        (0,0)
    ],
    [
        (0,3),
        (0,2),
        (0,1),
        (0,0)
    ],
    [
        (0,1),
        (0,0)
    ],
]

rocks_right_indices = [
    [
        (3,0)
    ],
    [
        (1,2),
        (2,1),
        (1,0)
    ],
    [
        (2,2),
        (2,1),
        (2,0)
    ],
    [
        (0,3),
        (0,2),
        (0,1),
        (0,0)
    ],
    [
        (1,1),
        (1,0)
    ],
]

rocks_down_indices = [
    [
        (0,0), (1, 0), (2, 0), (3, 0)
    ],
    [
        (0,1), (1, 0), (2, 1)
    ],
    [
        (0,0), (1, 0), (2, 0)
    ],
    [
        (0,0)
    ],
    [
        (0,0), (1, 0)
    ],
]

# make lower y correspond to lower pixels
for i, rock in enumerate(rocks):
    rocks[i].reverse()

for input_line in input_lines:
    input_line = input_line.strip()

    moves = input_line

num_rocks = 1000000000000
max_width = 7
max_height = 3

stack = [['.'] * max_width for _ in range(max_height+1)]

curr_height = 0
del_height = 0
move_i = 0

del_interval = 200000

height_diffs = []
heights = [0]
rocks_diff = []
rocks_done = [0]

for i in range(num_rocks):
    rock_i = i % 5
    rock = rocks[rock_i]
    rock_width = len(rock[0])
    rock_height = len(rock)

    x = 2

    for _ in range(3):
        # try to move left/right
        move = moves[move_i]
        move_i += 1
        if move_i == len(moves):
            move_i = 0
            height_diffs.append(curr_height - heights[-1])
            heights.append(curr_height)
            rocks_diff.append(i - rocks_done[-1])
            rocks_done.append(i)
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
        move_i += 1
        if move_i == len(moves):
            move_i = 0
            height_diffs.append(curr_height - heights[-1])
            heights.append(curr_height)
            rocks_diff.append(i - rocks_done[-1])
            rocks_done.append(i)
        if move == '>':
            if x + rock_width < max_width:
                horizontal_done = False
                indices = rocks_right_indices[rock_i]
                for index in indices:
                    rock_x, rock_y = index
                    check_x = x + rock_x + 1
                    if stack[y + rock_y - del_height][check_x] != '.':
                        horizontal_done = True
                        break
                if not horizontal_done:
                    x += 1
        else:
            if x > 0:
                horizontal_done = False
                indices = rocks_left_indices[rock_i]
                for index in indices:
                    rock_x, rock_y = index
                    check_x = x + rock_x - 1
                    if stack[y + rock_y - del_height][check_x] != '.':
                        horizontal_done = True
                        break
                if not horizontal_done:
                    x -= 1
        # try to move down
        indices = rocks_down_indices[rock_i]
        for index in indices:
            rock_x, rock_y = index
            check_y = y + rock_y - 1
            if check_y < 0 or stack[check_y - del_height][x + rock_x] != '.':
                done = True
                break
        if not done:
            y -= 1

    curr_height = max(curr_height, y + rock_height)

    for rock_y in range(rock_height):
        for rock_x in range(rock_width):
            if rock[rock_y][rock_x] == '#':
                stack[y + rock_y - del_height][x + rock_x] = '#'

    if len(stack) > del_interval:
        del_height += del_interval // 4
        del stack[:del_interval // 4]

    if curr_height >= max_height - 3:
        for _ in range(3):
            max_height += 1
            stack.append(['.'] * max_width)
    
    if len(height_diffs) >= 10:
        break

initial_height = sum(height_diffs[:5])
initial_rocks = sum(rocks_diff[:5])

add_heights = height_diffs[5:10]
add_rocks = rocks_diff[5:10]

whole_times = (num_rocks - initial_rocks) // sum(add_rocks)

total_height = initial_height + whole_times * sum(add_heights)
total_rocks = initial_rocks + whole_times * sum(add_rocks)

for i, add_rock in enumerate(add_rocks):
    if total_rocks + add_rock > num_rocks:
        break
    total_height += add_heights[i]
    total_rocks += add_rock

print(total_height, "-", total_height + add_heights[i], ",", total_rocks)
print(total_height + add_heights[i] * (num_rocks - total_rocks) / add_rocks[i])