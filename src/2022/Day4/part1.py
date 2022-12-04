from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day4/test.txt")

count = 0

for input_line in input_lines:
    elf1, elf2 = input_line.strip().split(",")

    elf1_start, elf1_end = elf1.split("-")
    elf1_start = (int)(elf1_start)
    elf1_end = (int)(elf1_end)
    elf2_start, elf2_end = elf2.split("-")
    elf2_start = (int)(elf2_start)
    elf2_end = (int)(elf2_end)
    
    if (elf1_start <= elf2_start and elf1_end >= elf2_end) or \
        (elf2_start <= elf1_start and elf2_end >= elf1_end):
        count += 1

print(count)