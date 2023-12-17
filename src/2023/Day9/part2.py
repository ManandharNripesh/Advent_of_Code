from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day9/test.txt")

extrapolated_values = []

for i, input_line in enumerate(input_lines):
    seq = [[int(x) for x in input_line.split()]]
    
    depth = 0
    final_value = 0

    # go down until all same
    while True:
        all_same = True
        final_value = seq[depth][0]
        for value in seq[depth]:
            if value != final_value:
                all_same = False
        if all_same:
            break
        seq.append([])
        for i in range(len(seq[depth]) - 1):
            seq[depth+1].append(seq[depth][i+1] - seq[depth][i])
        depth += 1
    
    # add new final value
    seq[depth].append(final_value)

    # go up to extrapolate next value
    while depth > 0:
        seq[depth-1].insert(0, seq[depth-1][0] - seq[depth][0])
        depth -= 1

    extrapolated_values.append(seq[0][0])

print(sum(extrapolated_values))