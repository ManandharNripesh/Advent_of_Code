from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day5/test.txt")

stacks = []
first = True
done_setup = False
num_stacks = 0

for input_line in input_lines:
    if input_line[-1] == '\n':
        input_line = input_line[:-1]
    if input_line == "":
        continue

    if first:
        first = False
        num_stacks = (len(input_line) // 4) + 1
        for _ in range(num_stacks):
            stacks.append([])

    if input_line[1] == '1':
        done_setup = True
        for i in range(num_stacks):
            stacks[i].reverse()
        continue
    else:
        if not done_setup:
            i = 0
            while i < len(input_line):
                if input_line[i] == '[':
                    stacks[i//4].append(input_line[i+1])
                i += 4
        else:
            i = 5
            j = i+1
            while input_line[j] != ' ':
                j += 1
            num_move = int(input_line[i:j])
            
            i = j+6
            j = i+1
            while input_line[j] != ' ':
                j += 1
            src = int(input_line[i:j]) - 1

            i = j+4
            dest = int(input_line[i:]) - 1

            to_move = stacks[src][-num_move:]
            for i in range(num_move):
                stacks[dest].append(to_move[i])
                stacks[src].pop()

for i in range(num_stacks):
    print(stacks[i][-1], end="")