from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day8/test.txt")

forest = []
forest_height = 0

for input_line in input_lines:
    input_line = input_line.strip()

    forest.append([int(x) for x in list(input_line)])
    forest_height += 1

forest_width = len(forest[0])

scores = [[0] * forest_width for i in range(forest_height)]

for i in range(1, forest_height - 1):
    for j in range(1, forest_width - 1):
        curr_tree = forest[i][j]
        
        count = 0
        for k in range(i-1, -1, -1):
            count += 1
            if forest[k][j] >= curr_tree:
                break
        scores[i][j] = count
        
        count = 0
        for k in range(i+1, forest_height):
            count += 1
            if forest[k][j] >= curr_tree:
                break
        scores[i][j] *= count
        
        count = 0
        for k in range(j-1, -1, -1):
            count += 1
            if forest[i][k] >= curr_tree:
                break
        scores[i][j] *= count
        
        count = 0
        for k in range(j+1, forest_width):
            count += 1
            if forest[i][k] >= curr_tree:
                break
        scores[i][j] *= count

print(max([max(row) for row in scores]))