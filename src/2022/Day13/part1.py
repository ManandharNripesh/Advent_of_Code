from ...common.input_reader import read_input
import ast

input_lines = read_input("src/2022/Day13/test.txt")

sum = 0
list1 = []
list2 = []

def compare_left_right(left, right):
    if type(left) is not list:
        if left == right:
            return -1
        return left < right

    for i in range(min(len(left), len(right))):
        ret_val = 0

        if type(left[i]) is list:
            if type(right[i]) is list:
                ret_val = compare_left_right(left[i], right[i])
            else:
                ret_val = compare_left_right(left[i], [right[i]])
        else:
            if type(right[i]) is list:
                ret_val = compare_left_right([left[i]], right[i])
            else:
                ret_val = compare_left_right(left[i], right[i])

        if ret_val == -1:
            continue
        else:
            return ret_val
    
    if len(left) == len(right):
        return -1
    return len(left) < len(right)

for line_num, input_line in enumerate(input_lines):
    input_line = input_line.strip()

    line_type = line_num % 3

    if line_type == 2:
        continue
    elif line_type == 0:
        list1 = ast.literal_eval(input_line)
    else: #elif line_type == 1:
        list2 =  ast.literal_eval(input_line)

        if compare_left_right(list1, list2):
            sum += line_num // 3 + 1

print(sum)