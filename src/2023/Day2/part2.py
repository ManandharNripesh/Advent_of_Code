from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day2/test.txt")

game_powers = []

for line_num, input_line in enumerate(input_lines):
    start_index = input_line.find(": ") + 2
    games_string = input_line[start_index:]
    games_list = games_string.split("; ")

    limits = {
        "red":0,
        "green": 0,
        "blue": 0
        } 

    for game in games_list:
        cubes_list = game.split(", ")
        for cube in cubes_list:
            cube_num, cube_color = cube.split(" ")
            if int(cube_num) > limits[cube_color.strip()]:
                limits[cube_color.strip()] = int(cube_num)
    
    game_powers.append(limits["red"] * limits["green"] * limits["blue"])

print(sum(game_powers))