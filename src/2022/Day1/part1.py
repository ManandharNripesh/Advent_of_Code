from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day1/test.txt")

elves = []
curr_elf = 0

for input_line in input_lines:
    if input_line == "\n":
        elves.append(curr_elf)
        curr_elf = 0
    else:
        curr_elf += int(input_line)

elves.append(curr_elf)

print(max(elves))