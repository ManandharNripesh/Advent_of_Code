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

total_time = 30 - 4

unopened_valves = set()
for valve in valves:
    if rates[valve] > 0 and dists["AA"][valve] < total_time:
        unopened_valves.add(valve)

# RECURSION: this time on just the unopened_valves
def calc_max_pressure(unopened, total, valve1, valve2, time1, time2):
    if len(unopened) == 0 or (time1 > total_time and time2 > total_time):
        return total
    
    # print(unopened)

    options = [total]

    unopened1 = unopened.copy()
    unopened2 = unopened.copy()

    if len(unopened) < 2:
        unopened1.add(valve1)
        unopened2.add(valve2)

    for next_valve in unopened:
        dist1 = dists[valve1][next_valve]
        dist2 = dists[valve2][next_valve]
        if dist1 < dist2:
            unopened2.remove(next_valve)
        elif dist2 < dist1:
            unopened1.remove(next_valve)

    for next_valve1 in unopened1:
        for next_valve2 in unopened2:
            if next_valve1 == next_valve2 or (next_valve1 == valve1 and next_valve2 == valve2):
                continue
            next_unopened = unopened.copy()

            next_time1 = time1
            next_time2 = time2
            next_total = total
            if next_valve1 != valve1:
                next_unopened.remove(next_valve1)
                next_time1 = time1 + dists[valve1][next_valve1] + 1
                next_total += rates[next_valve1] * (total_time - next_time1)
            if next_valve2 != valve2:
                next_unopened.remove(next_valve2)
                next_time2 = time2 + dists[valve2][next_valve2] + 1
                next_total += rates[next_valve2] * (total_time - next_time2)

            if next_time1 < total_time and next_time2 < total_time:
                options.append(calc_max_pressure(
                    next_unopened, next_total, next_valve1, next_valve2, next_time1, next_time2
                ))

    return max(options)

total_pressure = calc_max_pressure(unopened_valves, total_pressure, curr_valve, curr_valve, curr_time, curr_time)

print(total_pressure)