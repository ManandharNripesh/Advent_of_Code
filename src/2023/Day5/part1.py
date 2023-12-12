from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day5/test.txt")

class DataMapIndex:
    SEEDS                   = 0
    SEED_TO_SOIL            = 1
    SOIL_TO_FERTILIZER      = 2
    FERTILIZER_TO_WATER     = 3
    WATER_TO_LIGHT          = 4
    LIGHT_TO_TEMPERATURE    = 5
    TEMPERATURE_TO_HUMIDITY = 6
    HUMIDITY_TO_LOCATION    = 7

def getFirstItemInTuple(tuple):
    return(tuple[0])

data_maps = [[]]
data_maps_index = DataMapIndex.SEEDS
first_line = True

for input_line in input_lines:
    if input_line == "\n":
        if data_maps_index > 0:
            data_maps[data_maps_index].sort(key=getFirstItemInTuple)
        data_maps.append([])
        data_maps_index += 1
        first_line = True
        continue

    match data_maps_index:
        case DataMapIndex.SEEDS:
            _, data_maps[data_maps_index] = input_line.split(": ")
            data_maps[data_maps_index] = data_maps[data_maps_index].split()
            for i in range(len(data_maps[data_maps_index])):
                data_maps[data_maps_index][i] = int(data_maps[data_maps_index][i])
        case _:
            if first_line:
                first_line = False
                continue
            input_data = input_line.split()
            data_maps[data_maps_index].append((int(input_data[1]), int(input_data[0]), int(input_data[2])))

data_maps[-1].sort(key=getFirstItemInTuple)

#print(data_maps)

locations = []

for seed in data_maps[DataMapIndex.SEEDS]:
    value = seed
    for data_maps_index in range(DataMapIndex.SEED_TO_SOIL, DataMapIndex.HUMIDITY_TO_LOCATION + 1):
        #print(value)
        i = 0
        while i < len(data_maps[data_maps_index]) and value >= data_maps[data_maps_index][i][0]:
            i += 1
        if i > 0:
            diff = value - data_maps[data_maps_index][i-1][0]
            if diff - 1 <= data_maps[data_maps_index][i-1][2]:
                value = data_maps[data_maps_index][i-1][1] + diff
    locations.append(value)


#print(locations)
print(min(locations))