from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day3/test.txt")

schematic = []
part_numbers = []

for input_line in input_lines:
    schematic.append(input_line.strip())

for i, schematic_line in enumerate(schematic):
    j = 0
    while j < len(schematic_line):
        schematic_char = schematic_line[j]
        if schematic_char.isdigit():
            valid_part_number = False
            num_digits = 1
            while j + num_digits < len(schematic_line) and schematic_line[j+num_digits].isdigit():
                num_digits += 1
            num = int(schematic_line[j:j+num_digits])
            for i2 in range(i - 1, i + 2):
                if i2 == i:
                    for j2 in [j - 1, j + num_digits]:
                        if j2 >= 0 and j2 < len(schematic_line) and not schematic_line[j2].isdigit() and schematic_line[j2] != ".":
                            valid_part_number = True
                            break
                elif i2 >= 0 and i2 < len(schematic):
                    for j2 in range(j - 1, j + num_digits + 1):
                        if j2 >= 0 and j2 < len(schematic_line) and not schematic[i2][j2].isdigit() and schematic[i2][j2] != ".":
                            valid_part_number = True
                if valid_part_number:
                    break
            if valid_part_number:
                part_numbers.append(num)
            j += num_digits - 1
        j += 1

print(sum(part_numbers))