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
            _, seed_ranges = input_line.split(": ")
            seed_ranges = seed_ranges.split()
            for i in range(len(seed_ranges)):
                seed_ranges[i] = int(seed_ranges[i])
            for i in range(0, len(seed_ranges), 2):
                data_maps[data_maps_index].append((seed_ranges[i], seed_ranges[i+1]))
            data_maps[data_maps_index].sort(key=getFirstItemInTuple)
        case _:
            if first_line:
                first_line = False
                continue
            input_data = input_line.split()
            data_maps[data_maps_index].append((int(input_data[1]), int(input_data[0]), int(input_data[2])))

data_maps[-1].sort(key=getFirstItemInTuple)

locations = []

return_list = []

def split_ranges(data_maps_index, value_start, value_len):
    i = 0
    while i < len(data_maps[data_maps_index]) and value_start >= data_maps[data_maps_index][i][0]:
        i += 1
    i -= 1
    if i >= 0:
        if value_start >= data_maps[data_maps_index][i][0] + data_maps[data_maps_index][i][2]:
            if data_maps_index == DataMapIndex.HUMIDITY_TO_LOCATION:
                if i+1 < len(data_maps[data_maps_index]):
                    if value_start + value_len - 1 < data_maps[data_maps_index][i+1][0]:
                        return_list.append((value_start, value_len))
                    else:
                        value_start_1 = value_start
                        value_len_1 = data_maps[data_maps_index][i+1][0] - value_start
                        value_start_2 = value_start + value_len_1
                        value_len_2 = value_len - value_len_1
                        return_list.append((value_start_1, value_len_1))
                        split_ranges(data_maps_index, value_start_2, value_len_2)
                else:
                    return_list.append((value_start, value_len))
            else:
                if i+1 < len(data_maps[data_maps_index]):
                    if value_start + value_len - 1 < data_maps[data_maps_index][i+1][0]:
                        split_ranges(data_maps_index + 1, value_start, value_len)
                    else:
                        value_start_1 = value_start
                        value_len_1 = data_maps[data_maps_index][i+1][0] - value_start
                        value_start_2 = value_start + value_len_1
                        value_len_2 = value_len - value_len_1
                        split_ranges(data_maps_index + 1, value_start_1, value_len_1)
                        split_ranges(data_maps_index, value_start_2, value_len_2)
                else:
                    split_ranges(data_maps_index + 1, value_start, value_len)
        else:
            diff = value_start - data_maps[data_maps_index][i][0]
            if data_maps_index == DataMapIndex.HUMIDITY_TO_LOCATION:
                if value_start + value_len - 1 < data_maps[data_maps_index][i][0] + data_maps[data_maps_index][i][2]:
                    return_list.append((data_maps[data_maps_index][i][1] + diff, value_len))
                else:
                    value_start_1 = data_maps[data_maps_index][i][1] + diff
                    value_len_1 = data_maps[data_maps_index][i][2] - diff
                    value_start_2 = value_start + value_len_1
                    value_len_2 = value_len - value_len_1
                    return_list.append((value_start_1, value_len_1))
                    split_ranges(data_maps_index, value_start_2, value_len_2)
            else:
                if value_start + value_len - 1 < data_maps[data_maps_index][i][0] + data_maps[data_maps_index][i][2]:
                    split_ranges(data_maps_index + 1, data_maps[data_maps_index][i][1] + diff, value_len)
                else:
                    value_start_1 = data_maps[data_maps_index][i][1] + diff
                    value_len_1 = data_maps[data_maps_index][i][2] - diff
                    value_start_2 = value_start + value_len_1
                    value_len_2 = value_len - value_len_1
                    split_ranges(data_maps_index + 1, value_start_1, value_len_1)
                    split_ranges(data_maps_index, value_start_2, value_len_2)
    else:
        if data_maps_index == DataMapIndex.HUMIDITY_TO_LOCATION:
            if value_start + value_len - 1 < data_maps[data_maps_index][i+1][0]:
                return_list.append((value_start, value_len))
            else:
                value_start_1 = value_start
                value_len_1 = data_maps[data_maps_index][i+1][0] - value_start
                value_start_2 = value_start + value_len_1
                value_len_2 = value_len - value_len_1
                return_list.append((value_start_1, value_len_1))
                split_ranges(data_maps_index, value_start_2, value_len_2)
        else:
            if value_start + value_len - 1 < data_maps[data_maps_index][i+1][0]:
                split_ranges(data_maps_index + 1, value_start, value_len)
            else:
                value_start_1 = value_start
                value_len_1 = data_maps[data_maps_index][i+1][0] - value_start
                value_start_2 = value_start + value_len_1
                value_len_2 = value_len - value_len_1
                split_ranges(data_maps_index + 1, value_start_1, value_len_1)
                split_ranges(data_maps_index, value_start_2, value_len_2)

for seed_range in data_maps[DataMapIndex.SEEDS]:
    split_ranges(DataMapIndex.SEED_TO_SOIL, seed_range[0], seed_range[1])

return_list.sort(key=getFirstItemInTuple)

print(return_list[0][0])