from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day14/test.txt")

scan_map = set()
lowest_rock_y = 0

for input_line in input_lines:
    input_line = input_line.strip()

    words = input_line.split()

    points = words[::2]

    prev_x = -1
    prev_y = -1
    for point in points:
        x, y = point.split(",")
        x = int(x)
        y = int(y)

        if prev_y != -1:
            if x != prev_x:
                if prev_x < x:
                    for i in range(prev_x, x+1):
                        scan_map.add((i, y))
                else:
                    for i in range(x, prev_x+1):
                        scan_map.add((i, y))
            else:
                if prev_y < y:
                    for i in range(prev_y, y+1):
                        scan_map.add((x, i))
                else:
                    for i in range(y, prev_y+1):
                        scan_map.add((x, i))
        
        if y > lowest_rock_y:
            lowest_rock_y = y
        
        prev_x = x
        prev_y = y

source_x = 500
sand_count = 0
y = 0

while True:
    y = 0
    curr_x = source_x
    if (curr_x, 0) in scan_map:
        break
    scan_map.add((curr_x, y))

    while True:
        if y >= lowest_rock_y + 1:
            break
        scan_map.remove((curr_x, y))
        if (curr_x, y+1) not in scan_map:
            next
        elif (curr_x-1, y+1) not in scan_map:
            curr_x -= 1
        elif (curr_x+1, y+1) not in scan_map:
            curr_x += 1
        else:
            scan_map.add((curr_x, y))
            break
        y += 1
        scan_map.add((curr_x, y))

    
    sand_count += 1

print(sand_count)