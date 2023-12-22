from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day15/test.txt")

sequence = []

for i, input_line in enumerate(input_lines):
    sequence = input_line.strip().split(",")

def hash_func(string:str):
    ans = 0
    for char in string:
        ans += ord(char)
        ans *= 17
        ans %= 256
    return ans

boxes = [[] for _ in range(256)]

for step in sequence:
    label = ""
    num = 0
    if step[-1] == "-":
        label = step[:-1]
        box_num = hash_func(label)
        box = boxes[box_num]
        for i, lens in enumerate(box):
            if lens[0] == label:
                box.pop(i)
    else:
        label, num = step.split("=")
        num = int(num)
        box_num = hash_func(label)
        box = boxes[box_num]
        added = False
        for i, lens in enumerate(box):
            if lens[0] == label:
                box[i] = (label, num)
                added = True
                break
        if not added:
            box.append((label, num))

powers = []

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        powers.append((i+1) * (j+1) * lens[1])

print(sum(powers))