from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day14/test.txt")

platform = []

for i, input_line in enumerate(input_lines):
    platform.append(input_line.strip())

times = 1000000000

seen_platforms = {}
multiplied = False

i = 0
while i < times:
    if not multiplied and tuple(platform) in seen_platforms.keys():
        repeat_len = i - seen_platforms[tuple(platform)]
        multiplier = (times - i) // repeat_len
        i += multiplier * repeat_len
        multiplied = True
    seen_platforms[tuple(platform)] = i
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
    # tilt left
    for row in range(len(platform)):
        left_col = 0
        for col in range(len(platform[0])):
            match platform[row][col]:
                case "#":
                    left_col = col + 1
                case "O":
                    platform[row] = platform[row][:col] + "." + platform[row][col+1:]
                    platform[row] = platform[row][:left_col] + "O" + platform[row][left_col+1:]
                    left_col += 1
    # tilt down
    for col in range(len(platform[0])):
        lower_row = len(platform) - 1
        for row in range(len(platform)-1, -1, -1):
            match platform[row][col]:
                case "#":
                    lower_row = row - 1
                case "O":
                    platform[row] = platform[row][:col] + "." + platform[row][col+1:]
                    platform[lower_row] = platform[lower_row][:col] + "O" + platform[lower_row][col+1:]
                    lower_row -= 1
    # tilt right
    for row in range(len(platform)):
        right_col = len(platform[0]) - 1
        for col in range(len(platform[0])-1, -1, -1):
            match platform[row][col]:
                case "#":
                    right_col = col - 1
                case "O":
                    platform[row] = platform[row][:col] + "." + platform[row][col+1:]
                    platform[row] = platform[row][:right_col] + "O" + platform[row][right_col+1:]
                    right_col -= 1
    i += 1

# sum loads
load = 0
for i, platform_row in enumerate(platform):
    for space in platform_row:
        if space == "O":
            load += len(platform) - i

print(load)