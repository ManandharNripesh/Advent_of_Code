from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day10/test.txt")

cycle = 0
signal = 1
target_cycle = 20
total_strength = 0

for input_line in input_lines:
    input_line = input_line.strip()

    to_add = 0
    adding = False

    if input_line == "noop":
        cycle += 1
    else:
        _, to_add = input_line.split()
        to_add = int(to_add)
        cycle += 1
        adding = True

    if cycle == target_cycle:
        total_strength += signal * cycle
        print(to_add, signal, signal * cycle)
        target_cycle += 40
        if target_cycle > 220:
            break

    if adding:
        cycle += 1

    if cycle == target_cycle:
        total_strength += signal * cycle
        print(to_add, signal, signal * cycle)
        target_cycle += 40
        if target_cycle > 220:
            break

    if adding:
        signal += to_add

print(total_strength)