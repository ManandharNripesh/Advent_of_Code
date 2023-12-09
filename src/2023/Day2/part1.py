from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day2/test.txt")

limits = {
    "red":12,
    "green": 13,
    "blue": 14
    } 

possible_games = []

for line_num, input_line in enumerate(input_lines):
    start_index = input_line.find(": ") + 2
    games_string = input_line[start_index:]
    games_list = games_string.split("; ")

    possible = True
    for game in games_list:
        cubes_list = game.split(", ")
        for cube in cubes_list:
            cube_num, cube_color = cube.split(" ")
            if int(cube_num) > limits[cube_color.strip()]:
                possible = False
                break
        if not possible:
            break
    if possible:
        possible_games.append(line_num+1)

print(sum(possible_games))