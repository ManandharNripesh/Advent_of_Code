from ...common.input_reader import read_input

input_lines = read_input("src/2021/Day6/input.txt")

input_line = input_lines[0].split(",")

timers = [int(x) for x in input_line]

timers.sort()

# list of the number of fish in each time
counts = []
count = 0
for timer in timers:
    while (timer != len(counts)):
        counts.append(count)
        count = 0
    count += 1

while (len(counts) < 9):
    counts.append(count)
    count = 0

for _ in range(256):
    temp = counts[0]
    for i in range(8):
        counts[i] = counts[i+1]
    counts[6] += temp
    counts[8] = temp

print(sum(counts))
