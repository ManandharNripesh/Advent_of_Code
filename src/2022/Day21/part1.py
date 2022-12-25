from ...common.input_reader import read_input

input_lines = read_input("src/2022/Day21/test.txt")

monkeys = dict()
remaining_monkeys = set()

for input_line in input_lines:
    input_line = input_line.strip()

    words = input_line.split(":")

    monkey = words[0]
    value = words[1][1:]
    try:
        value = int(value)
    except ValueError:
        remaining_monkeys.add(monkey)
        pass

    monkeys[monkey] = value

while "root" in remaining_monkeys:
    next_remaining_monkeys = remaining_monkeys.copy()

    for monkey in remaining_monkeys:
        value = monkeys[monkey]

        left, op, right = value.split()

        if left in remaining_monkeys or right in remaining_monkeys:
            continue
        
        if op == "+":
            monkeys[monkey] = monkeys[left] + monkeys[right]
        elif op == "-":
            monkeys[monkey] = monkeys[left] - monkeys[right]
        elif op == "*":
            monkeys[monkey] = monkeys[left] * monkeys[right]
        elif op == "/":
            monkeys[monkey] = monkeys[left] / monkeys[right]

        next_remaining_monkeys.remove(monkey)

    remaining_monkeys = next_remaining_monkeys

print(int(monkeys["root"]))