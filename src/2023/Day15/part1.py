from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day15/test.txt")

sequence = []

for i, input_line in enumerate(input_lines):
    sequence = input_line.strip().split(",")

def hash_func(string:str):
    ans = 0
    for char in string:
        ans += ord(char)
        ans *= 17
        ans %= 256
    return ans

hashes = []

for step in sequence:
    hashes.append(hash_func(step))

print(sum(hashes))