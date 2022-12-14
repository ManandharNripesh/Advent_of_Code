from ...common.input_reader import read_input
import ast

input_lines = read_input("src/2022/Day13/test.txt")

packets = []
num_packets = 0

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

    curr_packet = []

    if line_type == 2:
        continue
    elif line_type == 0:
        curr_packet = ast.literal_eval(input_line)
    else: #elif line_type == 1:
        curr_packet =  ast.literal_eval(input_line)

    i = 0
    while i < num_packets:
        if compare_left_right(curr_packet, packets[i]):
            packets.insert(i, curr_packet)
            num_packets += 1
            break
        i += 1
    if i == num_packets:
        packets.append(curr_packet)
        num_packets += 1

decoder_key = 1

curr_packet = [[2]]
i = 0
while i < num_packets:
    if compare_left_right(curr_packet, packets[i]):
        packets.insert(i, curr_packet)
        break
    i += 1
if i == num_packets:
    packets.append(curr_packet)
    num_packets += 1
decoder_key *= i+1

curr_packet = [[6]]
i = 0
while i < num_packets:
    if compare_left_right(curr_packet, packets[i]):
        packets.insert(i, curr_packet)
        break
    i += 1
if i == num_packets:
    packets.append(curr_packet)
    num_packets += 1
decoder_key *= i+1

print(decoder_key)