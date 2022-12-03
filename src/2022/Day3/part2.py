from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day3/test.txt")

def char_to_pri(input_char):
    input_ascii = ord(input_char)
    if (input_ascii > ord("a")):
        return input_ascii - ord("a") + 1
    else:
        return input_ascii - ord("A") + 27

sum = 0
i = 0

while i < len(input_lines):
    bag1 = set(input_lines[i].strip())
    bag2 = set(input_lines[i+1].strip())
    bag3 = set(input_lines[i+2].strip())

    common_set = bag1.intersection(bag2)
    common_set = common_set.intersection(bag3)

    sum += char_to_pri(common_set.pop())

    i += 3

print(sum)