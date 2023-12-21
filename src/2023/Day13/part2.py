from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day13/test.txt")

pattern = []
columns_left = []
rows_above = []

def find_mirrors():
    found = False
    # check vertical reflection
    for col in range(len(pattern[0]) - 1):
        start = 0
        end = col+1
        if col >= len(pattern[0]) // 2:
            end = len(pattern[0]) - col - 1
        all_match = True
        one_off = False
        more_off = False
        for offset in range(start, end):
            col1 = [pattern_row[col-offset] for pattern_row in pattern]
            col2 = [pattern_row[col+offset+1] for pattern_row in pattern]
            if col1 != col2:
                all_match = False
                for index in range(len(col1)):
                    if col1[index] != col2[index]:
                        if not one_off:
                            one_off = True
                        else:
                            more_off = True
                            break
                if more_off:
                    break
        if not all_match and one_off and not more_off:
            columns_left.append(col + 1)
            found = True
            break

    if not found:
        # check horizontal reflection
        for row in range(len(pattern) - 1):
            start = 0
            end = row+1
            if row >= len(pattern) // 2:
                end = len(pattern) - row - 1
            all_match = True
            one_off = False
            more_off = False
            for offset in range(start, end):
                row1 = pattern[row-offset]
                row2 = pattern[row+offset+1]
                if row1 != row2:
                    all_match = False
                    for index in range(len(row1)):
                        if row1[index] != row2[index]:
                            if not one_off:
                                one_off = True
                            else:
                                more_off = True
                                break
                    if more_off:
                        break
            if not all_match and one_off and not more_off:
                rows_above.append(row + 1)
                found = True
                break

for i, input_line in enumerate(input_lines):
    if input_line.strip():
        pattern.append(input_line.strip())
    else:
        find_mirrors()
        pattern.clear()
find_mirrors()

print(sum(columns_left) + 100 * sum(rows_above))