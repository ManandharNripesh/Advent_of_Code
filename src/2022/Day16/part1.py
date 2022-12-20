from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day16/test.txt")

valves = set()
rates = dict()
tunnels = dict()

for input_line in input_lines:
    input_line = input_line.strip()

    words = input_line.split()

    valve = words[1]
    valves.add(valve)
    rates[valve] = int(words[4][5:-1])
    tunnel_strings = words[9:]
    tunnels[valve] = []

    for i, tunnel_string in enumerate(tunnel_strings):
        if i < len(tunnel_strings) - 1:
            tunnels[valve].append(tunnel_string[:-1])
        else:
            tunnels[valve].append(tunnel_string)


# first, find minimum all pairs distance
dists = dict()
for src in valves:
    valves_todo = [src]
    visited = set()
    dists[src] = dict()
    dists[src][src] = 0

    while len(valves_todo) > 0:
        curr_valve = valves_todo.pop(0)
        visited.add(curr_valve)
        for next_valve in tunnels[curr_valve]:
            if next_valve not in visited:
                valves_todo.append(next_valve)
                if next_valve in dists[src].keys():
                    if dists[src][curr_valve] + 1 < dists[src][next_valve]:
                        dists[src][next_valve] = dists[src][curr_valve] + 1
                else:
                    dists[src][next_valve] = dists[src][curr_valve] + 1

# then, find maximal pressure to release at each step
total_pressure = 0
curr_rate = 0
curr_valve = "AA"
curr_time = 0

total_time = 30

unopened_valves = set()
for valve in valves:
    if rates[valve] > 0 and dists["AA"][valve] < total_time:
        unopened_valves.add(valve)

# RECURSION: this time on just the unopened_valves
def calc_max_pressure(unopened, total, valve, time):
    if len(unopened) == 0 or time > total_time:
        return total
    
    options = [total]

    for next_valve in unopened:
        next_unopened = unopened.copy()
        next_unopened.remove(next_valve)
        
        next_time = time + dists[valve][next_valve] + 1
        next_total = total + rates[next_valve] * (total_time - next_time)
        if next_time < total_time:
            options.append(calc_max_pressure(
                next_unopened, next_total, next_valve, next_time
            ))
    
    return max(options)

total_pressure = calc_max_pressure(unopened_valves, total_pressure, curr_valve, curr_time)

print(total_pressure)