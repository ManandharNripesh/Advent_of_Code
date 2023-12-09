from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day1/test.txt")

calibrations = []

for input_line in input_lines:
    first_digit = 0
    last_digit = 0
    for c in input_line:
        if c.isdigit():
            first_digit = int(c)
            break
    for c in reversed(input_line):
        if c.isdigit():
            last_digit = int(c)
            break
    calibrations.append(first_digit * 10 + last_digit)

print(sum(calibrations))