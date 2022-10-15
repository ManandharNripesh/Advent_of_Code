from ...common.input_reader import read_input

input_lines = read_input("src/2021/Day6/input.txt")

input_line = input_lines[0].split(",")

timers = [int(x) for x in input_line]

for _ in range(80):
    new_fish_count = 0
    for i,timer in enumerate(timers):
        if timer == 0:
            timers[i] = 6
            new_fish_count += 1
        else:
            timers[i] -= 1
    timers.extend([8] * new_fish_count)

print(len(timers))
