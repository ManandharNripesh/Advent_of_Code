from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day3/test.txt")

schematic = []
gear_ratios = []

for input_line in input_lines:
    schematic.append(input_line.strip())

for i, schematic_line in enumerate(schematic):
    j = 0
    while j < len(schematic_line):
        schematic_char = schematic_line[j]
        if schematic_char == "*":
            adjacent_nums_i = []
            adjacent_nums_j = []
            adjacent_nums_len = []
            adjacent_nums = []
            for i2 in range(i - 1, i + 2):
                if i2 == i:
                    for j2 in [j - 1, j + 1]:
                        if j2 >= 0 and j2 < len(schematic_line) and schematic[i2][j2].isdigit():
                            if len(adjacent_nums) == 2:
                                adjacent_nums.append(0)
                                break
                            num_i = i2
                            num_j = j2
                            num_len = 1
                            while num_j - 1 >= 0 and schematic[num_i][num_j - 1].isdigit():
                                num_j -= 1
                                num_len += 1
                            while num_j + num_len < len(schematic[num_i]) and schematic[num_i][num_j + num_len].isdigit():
                                num_len += 1
                            num = int(schematic[num_i][num_j:num_j+num_len])

                            adjacent_nums_i.append(num_i)
                            adjacent_nums_j.append(num_j)
                            adjacent_nums_len.append(num_len)
                            adjacent_nums.append(num)
                elif i2 >= 0 and i2 < len(schematic):
                    j2 = j - 1
                    while j2 < j + 2:
                        j2_offset = 1
                        if j2 >= 0 and j2 < len(schematic_line) and schematic[i2][j2].isdigit():
                            if len(adjacent_nums) == 2:
                                adjacent_nums.append(0)
                                break
                            num_i = i2
                            num_j = j2
                            num_len = 1
                            while num_j - 1 >= 0 and schematic[num_i][num_j - 1].isdigit():
                                num_j -= 1
                                num_len += 1
                            while num_j + num_len < len(schematic[num_i]) and schematic[num_i][num_j + num_len].isdigit():
                                num_len += 1
                                j2_offset += 1
                            num = int(schematic[num_i][num_j:num_j+num_len])

                            adjacent_nums_i.append(num_i)
                            adjacent_nums_j.append(num_j)
                            adjacent_nums_len.append(num_len)
                            adjacent_nums.append(num)
                        j2 += j2_offset
                if len(adjacent_nums) > 2:
                    break
            if len(adjacent_nums) == 2:
                gear_ratios.append(adjacent_nums[0] * adjacent_nums[1])
        j += 1

print(sum(gear_ratios))