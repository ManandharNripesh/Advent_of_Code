from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day3/test.txt")

def char_to_pri(input_char):
    input_ascii = ord(input_char)
    if (input_ascii > ord("a")):
        return input_ascii - ord("a") + 1
    else:
        return input_ascii - ord("A") + 27

sum = 0

for input_line in input_lines:
    input_line = input_line.strip()
    line_len = len(input_line)
    part1 = input_line[:line_len // 2]
    part2 = input_line[line_len // 2:]
    set1 = set(part1)
    set2 = set(part2)
    common_set = set1.intersection(set2)
    if (len(common_set) != 1):
        print("ERROR:")
    sum += char_to_pri(common_set.pop())

print(sum)