from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day20/test.txt")

original_numbers = []
i = 0

for input_line in input_lines:
    input_line = input_line.strip()
    
    # original_numbers.append((int(input_line), i))
    original_numbers.append((int(input_line) * 811589153, i))
    i += 1

mixed_numbers = original_numbers.copy()

for _ in range(10):
    for original_index, original_node in enumerate(original_numbers):
        number, _ = original_node
        if number == 0:
            continue

        mixed_index = 0
        for i, node in enumerate(mixed_numbers):
            number, original_i = node
            if original_i == original_index:
                mixed_index = i
                break

        node = mixed_numbers.pop(mixed_index)

        new_index = (mixed_index + number) % len(mixed_numbers)

        # this is just to match how test input looks like (same list though)
        if new_index == 0:
            new_index = len(mixed_numbers)

        mixed_numbers.insert(new_index, node)

zero_index = 0
for i, node in enumerate(mixed_numbers):
    number, original_i = node
    if number == 0:
        zero_index = i
        break
sum = 0
for i in range(1000, 3001, 1000):
    num = mixed_numbers[(zero_index + i) % len(mixed_numbers)][0]
    # print(num)
    sum += num

print(sum)