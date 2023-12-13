from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day6/test.txt")

times = []
distances = []

for i, input_line in enumerate(input_lines):
    _, data = input_line.split(": ")
    data = data.split()
    for j in range(len(data)):
        data[j] = int(data[j])
    match i:
        case 0:
            times = data.copy()
        case 1:
            distances = data.copy()

ways_to_win = []

for i in range(len(times)):
    count = 0
    for j in range(1, times[i]):
        distance = j * (times[i] - j)
        if distance > distances[i]:
            count += 1
    ways_to_win.append(count)

answer = 1

for i in ways_to_win:
    answer *= i

print(answer)