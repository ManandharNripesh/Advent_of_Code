from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day4/test.txt")

cards = [1] * len(input_lines)

for i, input_line in enumerate(input_lines):
    _, input_line = input_line.split(": ")
    winning_numbers, have_numbers = input_line.split(" | ")
    winning_numbers_set = set(winning_numbers.split())
    have_numbers_set =  set(have_numbers.split())
    matches_set = winning_numbers_set.intersection(have_numbers_set)
    if len(matches_set) > 0:
        for j in range(i+1, i+1+len(matches_set)):
            if j >= len(cards):
                break
            cards[j] += cards[i]

print(sum(cards))