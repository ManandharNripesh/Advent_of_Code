from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day4/test.txt")

points = []

for input_line in input_lines:
    _, input_line = input_line.split(": ")
    winning_numbers, have_numbers = input_line.split(" | ")
    winning_numbers_set = set(winning_numbers.split())
    have_numbers_set =  set(have_numbers.split())
    matches_set = winning_numbers_set.intersection(have_numbers_set)
    if len(matches_set) > 0:
        points.append(2 ** (len(matches_set) - 1))
    else:
        points.append(0)

print(sum(points))