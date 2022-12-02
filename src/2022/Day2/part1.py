from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day2/test.txt")

the_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

score = 0
for input_line in input_lines:
    opp, you = input_line.strip().split(" ")
    if the_map[you] == the_map[opp]:
        score += the_map[you] + 3
    else:
        if the_map[you] == 1 and the_map[opp] == 3:
            score += the_map[you] + 6
        elif the_map[you] == 3 and the_map[opp] == 1:
            score += the_map[you]
        elif the_map[you] > the_map[opp]:
            score += the_map[you] + 6
        elif the_map[you] < the_map[opp]:
            score += the_map[you]
        else:
            print("ERROR")

print(score)