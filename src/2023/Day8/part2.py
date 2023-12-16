from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day8/test.txt")

directions = ""
nodes_left = {}
nodes_right = {}

for i, input_line in enumerate(input_lines):
    match i:
        case 0:
            directions = input_line.strip()
        case 1:
            continue
        case _:
            start_node, left_right = input_line.strip().split(" = ")
            left_right = left_right[1:-1]
            left, right = left_right.split(", ")
            nodes_left[start_node] = left
            nodes_right[start_node] = right

start_nodes = []
for node in nodes_left.keys():
    if node[-1] == "A":
        start_nodes.append(node)

nodes_reached_Z = {}
first_repeat_index = {}

for node in start_nodes:
    cur_node = node
    step = 0
    steps_since_last_Z = 0
    while True:
        cur_dir = directions[step % len(directions)]
        if cur_dir == "L":
            cur_node = nodes_left[cur_node]
        else:
            cur_node = nodes_right[cur_node]
        step += 1
        steps_since_last_Z += 1
        if cur_node[-1] == "Z":
            if node in nodes_reached_Z.keys():
                for i, node_step_steps_last_Z in enumerate(nodes_reached_Z[node]):
                    if (cur_node, step % len(directions), steps_since_last_Z) == node_step_steps_last_Z:
                        first_repeat_index[node] = i
                        break
                if node in first_repeat_index:
                    break
                else:
                    nodes_reached_Z[node].append((cur_node, step % len(directions), steps_since_last_Z))
            else:
                nodes_reached_Z[node] = [(cur_node, step % len(directions), steps_since_last_Z)]
            steps_since_last_Z = 0

nodes = start_nodes.copy()
steps = {}
nodes_index = {}
for node in start_nodes:
    steps[node] = nodes_reached_Z[node][0][2]
    nodes_index[node] = 0

reached_Z = False


factors = {}
# https://byjus.com/maths/prime-numbers/
primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
 ]
for step in steps.values():
    factors[step] = {}
    value = step
    for i in primes:
        factors[step][i] = 0
    for i in primes:
        # print(value)
        done = False
        while value % i == 0:
            value /= i
            factors[step][i] += 1
            if value == 1:
                done = True
                break
        if done:
            break

max_factors = {}
for factor in primes:
    max_factors[factor] = 0
for factor in primes:
    for step in steps.values():
        max_factors[factor] = max(factors[step][factor], max_factors[factor])
step = 1
for factor in primes:
    step *= factor ** max_factors[factor]

print(step)