from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day11/test.txt")

inspections = []
items = []
ops = []
tests = []
next_monkeys = []

line_num = 0

for input_line in input_lines:
    input_words = input_line.strip().split()

    if line_num == 0:
        inspections.append(0)
    elif line_num == 1:
        items.append([])
        for i in range(2, len(input_words) - 1):
            items[-1].append(int(input_words[i][:-1]))
        items[-1].append(int(input_words[-1]))
    elif line_num == 2:
        ops.append([input_words[4], input_words[5]])
    elif line_num == 3:
        tests.append(int(input_words[3]))
    elif line_num == 4:
        next_monkeys.append([-1, int(input_words[5])])
    elif line_num == 5:
        next_monkeys[-1][0] = int(input_words[5])
    elif line_num == 6:
        next
    
    line_num = (line_num + 1) % 7

num_monkeys = len(inspections)

divisor = 1
for test in tests:
    divisor *= test

for i in range(10000):
    for j in range(num_monkeys):
        for item in items[j]:
            new_item = item
            # operation
            if ops[j][0] == "+":
                new_item += int(ops[j][1])
            elif ops[j][0] == "*":
                if ops[j][1] == "old":
                    new_item *= new_item
                else:
                    new_item *= int(ops[j][1])
            # divide worry
            new_item %= divisor
            # test
            condition = int(new_item % tests[j] == 0)
            items[next_monkeys[j][condition]].append(new_item)
            inspections[j] += 1
        items[j].clear()

max1 = 0
max2 = 0

for inspection in inspections:
    if inspection > max1:
        max2 = max1
        max1 = inspection
    elif inspection > max2:
        max2 = inspection

print(max1 * max2)