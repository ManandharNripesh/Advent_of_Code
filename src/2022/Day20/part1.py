from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day20/test.txt")

original_numbers = []

for input_line in input_lines:
    input_line = input_line.strip()
    
    original_numbers.append(int(input_line))

indices = [i for i in range(len(original_numbers))]
mixed_numbers = original_numbers.copy()

for original_index, number in enumerate(original_numbers):
    if number == 0:
        continue

    mixed_index = indices[original_index]

    mixed_numbers.pop(mixed_index)

    new_index = (mixed_index + number) % len(mixed_numbers)

    # this is just to match how test input looks like (same list though)
    if new_index == 0:
        new_index = len(mixed_numbers)
    
    if new_index < mixed_index:
        for i in range(new_index, mixed_index):
            indices_index = indices.index(i)
            indices[indices_index] += 1
    elif new_index > mixed_index:
        for i in range(mixed_index, new_index+1):
            indices_index = indices.index(i)
            indices[indices_index] -= 1
    indices[original_index] = new_index

    mixed_numbers.insert(new_index, number)

zero_index = mixed_numbers.index(0)
sum = 0
for i in range(1000, 3001, 1000):
    num = mixed_numbers[(zero_index + i) % len(mixed_numbers)]
    # print(num)
    sum += num

print(sum)