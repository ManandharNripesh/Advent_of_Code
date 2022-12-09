from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day9/test.txt")

positions = set()

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

positions.add((tail_x, tail_y))

for input_line in input_lines:
    input_line = input_line.strip()

    direction, steps = input_line.split()

    steps = int(steps)

    if direction == "R":
        for _ in range(steps):
            head_x += 1
            if abs(head_x - tail_x) > 1:
                tail_x += 1
                if head_y - tail_y >= 1:
                    tail_y += 1
                elif tail_y - head_y >= 1:
                    tail_y -= 1
            positions.add((tail_x, tail_y))
    elif direction == "L":
        for _ in range(steps):
            head_x -= 1
            if abs(head_x - tail_x) > 1:
                tail_x -= 1
                if head_y - tail_y >= 1:
                    tail_y += 1
                elif tail_y - head_y >= 1:
                    tail_y -= 1
            positions.add((tail_x, tail_y))
    elif direction == "U":
        for _ in range(steps):
            head_y += 1
            if abs(head_y - tail_y) > 1:
                tail_y += 1
                if head_x - tail_x >= 1:
                    tail_x += 1
                elif tail_x - head_x >= 1:
                    tail_x -= 1
            positions.add((tail_x, tail_y))
    elif direction == "D":
        for _ in range(steps):
            head_y -= 1
            if abs(head_y - tail_y) > 1:
                tail_y -= 1
                if head_x - tail_x >= 1:
                    tail_x += 1
                elif tail_x - head_x >= 1:
                    tail_x -= 1
            positions.add((tail_x, tail_y))

print(len(positions))