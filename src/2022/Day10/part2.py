from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day10/test.txt")

cycle = 0
signal = 1

screen = ['.']*6*40

for input_line in input_lines:
    input_line = input_line.strip()

    if cycle % 40 == signal or cycle % 40 == signal - 1 or cycle % 40 == signal + 1:
        screen[cycle] = '#'

    if input_line == "noop":
        cycle += 1
        continue
    # else:
    _, to_add = input_line.split()
    to_add = int(to_add)
    cycle += 1

    if cycle % 40 == signal or cycle % 40 == signal - 1 or cycle % 40 == signal + 1:
        screen[cycle] = '#'

    signal += to_add
    
    cycle += 1
    
for i in range(6):
    for j in range(40):
        print(screen[i*40+j], end="")
    print()