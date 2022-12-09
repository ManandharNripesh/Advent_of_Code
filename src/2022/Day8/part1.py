from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day8/test.txt")

forest = []
forest_height = 0

for input_line in input_lines:
    input_line = input_line.strip()

    forest.append(list(input_line))
    forest_height += 1

forest_width = len(forest[0])

visible_trees = 2*(forest_width + forest_height) - 4

for i in range(1, forest_height - 1):
    for j in range(1, forest_width - 1):
        curr_tree = forest[i][j]

        visible = True
        for k in range(i):
            if forest[k][j] >= curr_tree:
                visible = False
                break
        if visible:
            visible_trees += 1
            continue
        
        visible = True
        for k in range(i+1, forest_height):
            if forest[k][j] >= curr_tree:
                visible = False
                break
        if visible:
            visible_trees += 1
            continue
        
        visible = True
        for k in range(j):
            if forest[i][k] >= curr_tree:
                visible = False
                break
        if visible:
            visible_trees += 1
            continue
        
        visible = True
        for k in range(j+1, forest_width):
            if forest[i][k] >= curr_tree:
                visible = False
                break
        if visible:
            visible_trees += 1
            continue

print(visible_trees)