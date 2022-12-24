from ...common.input_reader import read_input

import math

input_lines = read_input("src/2022/Day19/test.txt")

blueprints = []

# enum for robot/material types
ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

for input_line in input_lines:
    input_line = input_line.strip()

    words = input_line.split()

    blueprint = [[0] * 4 for _ in range(4)]

    blueprint[ORE][ORE] = int(words[6])

    blueprint[CLAY][ORE] = int(words[12])
    
    blueprint[OBSIDIAN][ORE] = int(words[18])
    blueprint[OBSIDIAN][CLAY] = int(words[21])

    blueprint[GEODE][ORE] = int(words[27])
    blueprint[GEODE][OBSIDIAN] = int(words[30])

    blueprints.append(blueprint)

max_time = 32
decisions = []

def calc_max_geode( blueprint, ore=0, ore_rate=1, clay=0, clay_rate=0, \
                    obsidian=0, obsidian_rate=0, geode=0, geode_rate=0, \
                    time=0):
    if time >= max_time:
        return geode

    options = []

    max_ore_rate = max(
        blueprint[ORE][ORE],
        blueprint[CLAY][ORE],
        blueprint[OBSIDIAN][ORE],
        blueprint[GEODE][ORE]
    )

    # make ore bot
    if ore_rate < max_ore_rate and obsidian_rate == 0:
        diff = math.ceil((blueprint[ORE][ORE] - ore) / ore_rate)
        dt = 1
        if diff > 0:
            dt += diff
        next_time = time + dt
        if next_time < max_time:
            next_ore = ore + ore_rate * dt - blueprint[ORE][ORE]
            next_clay = clay + clay_rate * dt
            next_obsidian = obsidian + obsidian_rate * dt
            next_geode = geode + geode_rate * dt
            options.append(calc_max_geode(  blueprint, next_ore, ore_rate+1, next_clay, clay_rate,
                                            next_obsidian, obsidian_rate, next_geode, geode_rate, next_time))
    # make clay bot
    if clay_rate < blueprint[OBSIDIAN][CLAY] and geode_rate == 0:
        diff = math.ceil((blueprint[CLAY][ORE] - ore) / ore_rate)
        dt = 1
        if diff > 0:
            dt += diff
        next_time = time + dt
        if next_time < max_time:
            next_ore = ore + ore_rate * dt - blueprint[CLAY][ORE]
            next_clay = clay + clay_rate * dt
            next_obsidian = obsidian + obsidian_rate * dt
            next_geode = geode + geode_rate * dt
            options.append(calc_max_geode(  blueprint, next_ore, ore_rate, next_clay, clay_rate+1,
                                            next_obsidian, obsidian_rate, next_geode, geode_rate, next_time))
    # make obsidian bot
    if clay_rate > 0 and obsidian_rate < blueprint[GEODE][OBSIDIAN]:
        diff = max( math.ceil((blueprint[OBSIDIAN][ORE] - ore) / ore_rate),
                    math.ceil((blueprint[OBSIDIAN][CLAY] - clay) / clay_rate))
        dt = 1
        if diff > 0:
            dt += diff
        next_time = time + dt
        if next_time < max_time:
            next_ore = ore + ore_rate * dt - blueprint[OBSIDIAN][ORE]
            next_clay = clay + clay_rate * dt - blueprint[OBSIDIAN][CLAY]
            next_obsidian = obsidian + obsidian_rate * dt
            next_geode = geode + geode_rate * dt
            options.append(calc_max_geode(  blueprint, next_ore, ore_rate, next_clay, clay_rate,
                                            next_obsidian, obsidian_rate+1, next_geode, geode_rate, next_time))
    # make geode bot
    if obsidian_rate > 0:
        diff = max( math.ceil((blueprint[GEODE][ORE] - ore) / ore_rate),
                    math.ceil((blueprint[GEODE][OBSIDIAN] - obsidian) / obsidian_rate))
        dt = 1
        if diff > 0:
            dt += diff
        next_time = time + dt
        if next_time < max_time:
            next_ore = ore + ore_rate * dt - blueprint[GEODE][ORE]
            next_clay = clay + clay_rate * dt
            next_obsidian = obsidian + obsidian_rate * dt - blueprint[GEODE][OBSIDIAN]
            next_geode = geode + geode_rate * dt
            options.append(calc_max_geode(  blueprint, next_ore, ore_rate, next_clay, clay_rate,
                                            next_obsidian, obsidian_rate, next_geode, geode_rate+1, next_time))

    if len(options) == 0:
        dt = max_time - time
        return geode + geode_rate * dt

    return max(options)

max_geode_list = []

for i,blueprint in enumerate(blueprints):
    if i > 2:
        break
    max_geode_list.append(calc_max_geode(blueprint))

quality = 1
for i, max_geode in enumerate(max_geode_list):
    quality *= max_geode

print(quality)