from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day1/test.txt")

calibrations = []

for input_line in input_lines:
    first_digit = 0
    last_digit = 0
    for i, c in enumerate(input_line):
        if c.isdigit():
            first_digit = int(c)
            break
        else:
            match c:
                case "o":
                    if i <= len(input_line) - 3 and input_line[i:i+3] == "one":
                        first_digit = 1
                        break
                case "t":
                    if i <= len(input_line) - 3 and input_line[i:i+3] == "two":
                        first_digit = 2
                        break
                    if i <= len(input_line) - 5 and input_line[i:i+5] == "three":
                        first_digit = 3
                        break
                case "f":
                    if i <= len(input_line) - 4 and input_line[i:i+4] == "four":
                        first_digit = 4
                        break
                    if i <= len(input_line) - 4 and input_line[i:i+4] == "five":
                        first_digit = 5
                        break
                case "s":
                    if i <= len(input_line) - 3 and input_line[i:i+3] == "six":
                        first_digit = 6
                        break
                    if i <= len(input_line) - 5 and input_line[i:i+5] == "seven":
                        first_digit = 7
                        break
                case "e":
                    if i <= len(input_line) - 5 and input_line[i:i+5] == "eight":
                        first_digit = 8
                        break
                case "n":
                    if i <= len(input_line) - 4 and input_line[i:i+4] == "nine":
                        first_digit = 9
                        break
    for i, c in enumerate(reversed(input_line)):
        if c.isdigit():
            last_digit = int(c)
            break
        else:
            match c:
                case "o":
                    if i >= 3 and input_line[-i-1:][:3] == "one":
                        last_digit = 1
                        break
                case "t":
                    if i >= 3 and input_line[-i-1:][:3] == "two":
                        last_digit = 2
                        break
                    if i >= 5 and input_line[-i-1:][:5] == "three":
                        last_digit = 3
                        break
                case "f":
                    if i >= 4 and input_line[-i-1:][:4] == "four":
                        last_digit = 4
                        break
                    if i >= 4 and input_line[-i-1:][:4] == "five":
                        last_digit = 5
                        break
                case "s":
                    if i >= 3 and input_line[-i-1:][:3] == "six":
                        last_digit = 6
                        break
                    if i >= 5 and input_line[-i-1:][:5] == "seven":
                        last_digit = 7
                        break
                case "e":
                    if i >= 5 and input_line[-i-1:][:5] == "eight":
                        last_digit = 8
                        break
                case "n":
                    if i >= 4 and input_line[-i-1:][:4] == "nine":
                        last_digit = 9
                        break
    calibrations.append(first_digit * 10 + last_digit)

print(sum(calibrations))