from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day9/test.txt")

positions = set()

knots = 10

x = [0] * knots
y = [0] * knots

positions.add((x[knots - 1], y[knots - 1]))

for input_line in input_lines:
    input_line = input_line.strip()

    direction, steps = input_line.split()

    steps = int(steps)

    if direction == "R":
        for _ in range(steps):
            x[0] += 1
            for i in range(knots - 1):
                if abs(x[i] - x[i+1]) > 1:
                    if x[i] > x[i+1]:
                        x[i+1] += 1
                    else:
                        x[i+1] -= 1
                    if y[i] - y[i+1] >= 1:
                        y[i+1] += 1
                    elif y[i+1] - y[i] >= 1:
                        y[i+1] -= 1
                if abs(y[i] - y[i+1]) > 1:
                    if y[i] > y[i+1]:
                        y[i+1] += 1
                    else:
                        y[i+1] -= 1
                    if x[i] - x[i+1] >= 1:
                        x[i+1] += 1
                    elif x[i+1] - x[i] >= 1:
                        x[i+1] -= 1
            positions.add((x[knots - 1], y[knots - 1]))
    elif direction == "L":
        for _ in range(steps):
            x[0] -= 1
            for i in range(knots - 1):
                if abs(x[i] - x[i+1]) > 1:
                    if x[i] > x[i+1]:
                        x[i+1] += 1
                    else:
                        x[i+1] -= 1
                    if y[i] - y[i+1] >= 1:
                        y[i+1] += 1
                    elif y[i+1] - y[i] >= 1:
                        y[i+1] -= 1
                if abs(y[i] - y[i+1]) > 1:
                    if y[i] > y[i+1]:
                        y[i+1] += 1
                    else:
                        y[i+1] -= 1
                    if x[i] - x[i+1] >= 1:
                        x[i+1] += 1
                    elif x[i+1] - x[i] >= 1:
                        x[i+1] -= 1
            positions.add((x[knots - 1], y[knots - 1]))
    elif direction == "U":
        for _ in range(steps):
            y[0] += 1
            for i in range(knots - 1):
                if abs(x[i] - x[i+1]) > 1:
                    if x[i] > x[i+1]:
                        x[i+1] += 1
                    else:
                        x[i+1] -= 1
                    if y[i] - y[i+1] >= 1:
                        y[i+1] += 1
                    elif y[i+1] - y[i] >= 1:
                        y[i+1] -= 1
                if abs(y[i] - y[i+1]) > 1:
                    if y[i] > y[i+1]:
                        y[i+1] += 1
                    else:
                        y[i+1] -= 1
                    if x[i] - x[i+1] >= 1:
                        x[i+1] += 1
                    elif x[i+1] - x[i] >= 1:
                        x[i+1] -= 1
            positions.add((x[knots - 1], y[knots - 1]))
    elif direction == "D":
        for _ in range(steps):
            y[0] -= 1
            for i in range(knots - 1):
                if abs(x[i] - x[i+1]) > 1:
                    if x[i] > x[i+1]:
                        x[i+1] += 1
                    else:
                        x[i+1] -= 1
                    if y[i] - y[i+1] >= 1:
                        y[i+1] += 1
                    elif y[i+1] - y[i] >= 1:
                        y[i+1] -= 1
                if abs(y[i] - y[i+1]) > 1:
                    if y[i] > y[i+1]:
                        y[i+1] += 1
                    else:
                        y[i+1] -= 1
                    if x[i] - x[i+1] >= 1:
                        x[i+1] += 1
                    elif x[i+1] - x[i] >= 1:
                        x[i+1] -= 1
            positions.add((x[knots - 1], y[knots - 1]))

print(len(positions))