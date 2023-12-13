from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day6/test.txt")

times = 0
distances = 0

for i, input_line in enumerate(input_lines):
    _, data = input_line.split(": ")
    data = data.split()
    data = "".join(data)
    data = int(data)
    match i:
        case 0:
            times = data
        case 1:
            distances = data

ways_to_win = 0

for j in range(1, times):
    distance = j * (times - j)
    if distance > distances:
        ways_to_win += 1

print(ways_to_win)