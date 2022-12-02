from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day2/test.txt")

the_map = {
    "A": 1,
    "B": 2,
    "C": 3
}

score = 0
for input_line in input_lines:
    opp, you = input_line.strip().split(" ")
    
    if you == "X":
        choice = the_map[opp] - 1
        if choice < 1:
            choice += 3
        score += choice
    elif you == "Y":
        choice = the_map[opp]
        score += choice + 3
    elif you == "Z":
        choice = the_map[opp] + 1
        if choice > 3:
            choice -= 3
        score += choice + 6
    else:
        print("ERROR")

print(score)