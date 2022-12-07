from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day6/test.txt")

input_line = input_lines[0]


recent_chars = []
for i in range(14):
    recent_chars.append(input_line[i])

if len(set(recent_chars)) == 14:
    print(14)
else:
    for i in range(14, len(input_line)):
        recent_chars.pop(0)
        recent_chars.append(input_line[i])
        if len(set(recent_chars)) == 14:
            print(i+1)
            exit()