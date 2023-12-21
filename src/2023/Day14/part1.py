from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day14/test.txt")

platform = []

for i, input_line in enumerate(input_lines):
    platform.append(input_line.strip())

# tilt up
for col in range(len(platform[0])):
    upper_row = 0
    for row in range(len(platform)):
        match platform[row][col]:
            case "#":
                upper_row = row + 1
            case "O":
                platform[row] = platform[row][:col] + "." + platform[row][col+1:]
                platform[upper_row] = platform[upper_row][:col] + "O" + platform[upper_row][col+1:]
                upper_row += 1

# sum loads
load = 0
for i, platform_row in enumerate(platform):
    for space in platform_row:
        if space == "O":
            load += len(platform) - i

print(load)