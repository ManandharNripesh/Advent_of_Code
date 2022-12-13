from ...common.input_reader import read_input
import heapq


input_lines = read_input("src/2022/Day12/test.txt")

def char_to_int(lchar):
    return ord(lchar) - ord('a')

the_map = []

num_rows = 0
start_index = (-1, -1)
end_index = (-1, -1)

for input_line in input_lines:
    input_line = input_line.strip()

    the_map.append(list(input_line))
    num_rows += 1

    for i, height in enumerate(the_map[-1]):
        if height == 'S':
            the_map[-1][i] = 'a'
            start_index = (num_rows - 1, i)
        if height == 'E':
            the_map[-1][i] = 'z'
            end_index = (num_rows - 1, i)

the_map_num = []

for row in the_map:
    the_map_num.append([])
    for height in row:
        the_map_num[-1].append(char_to_int(height))

next_squares_list = []

for j, row in enumerate(the_map_num):
    next_squares_list.append([])
    for i, height in enumerate(row):
        next_squares_list[-1].append([])
        
        if i > 0 and row[i-1] <= height + 1:
            next_squares_list[-1][-1].append((j, i-1))
        if i < len(row)-1 and row[i+1] <= height + 1:
            next_squares_list[-1][-1].append((j, i+1))
        if j > 0 and the_map_num[j-1][i] <= height + 1:
            next_squares_list[-1][-1].append((j-1, i))
        if j < num_rows-1 and the_map_num[j+1][i] <= height + 1:
            next_squares_list[-1][-1].append((j+1, i))

sptSet = [[False] * len(the_map_num[0]) for _ in the_map_num]

squares_heap = []

final_distance = 0

for j, row in enumerate(the_map):
    for i, height in enumerate(row):
        if (j, i) == start_index:
            heapq.heappush(squares_heap, (0, j, i))
        else:
            heapq.heappush(squares_heap, (999999, j, i))

while len(squares_heap) != 0:
    distance, j, i = heapq.heappop(squares_heap)

    for next_j, next_i in next_squares_list[j][i]:
        # check if next is in squares_heap
        for heap_index, (heap_d, heap_j, heap_i) in enumerate(squares_heap):
            if (heap_j, heap_i) == (next_j, next_i):
                # update distance
                if distance + 1 < heap_d:
                    squares_heap.pop(heap_index)
                    heapq.heapify(squares_heap)
                    heapq.heappush(squares_heap, (distance + 1, heap_j, heap_i))
                    if (next_j, next_i) == end_index:
                        final_distance = distance + 1
                break

print(final_distance)