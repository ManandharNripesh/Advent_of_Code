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
        if monkey == "root":
            value = value[:5] + "=" + value[6:]
        pass

    if monkey == "humn":
        remaining_monkeys.add(monkey)
        continue

    monkeys[monkey] = value

changed = True

while "root" in remaining_monkeys and changed:
    changed = False
    next_remaining_monkeys = remaining_monkeys.copy()

    for monkey in remaining_monkeys:
        if monkey == "humn":
            continue
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
            monkeys[monkey] = monkeys[left] // monkeys[right]

        next_remaining_monkeys.remove(monkey)

    if len(remaining_monkeys) != len(next_remaining_monkeys):
        remaining_monkeys = next_remaining_monkeys
        changed = True

my_value = 0
monkey = "root"
left, op, right = monkeys[monkey].split()
if left not in remaining_monkeys:
    my_value = monkeys[left]
    monkey = right
elif right not in remaining_monkeys:
    my_value = monkeys[right]
    monkey = left
else:
    print("ERROR!")

while monkey != "humn":
    left, op, right = monkeys[monkey].split()

    if op == "+":
        if left not in remaining_monkeys:
            my_value -= monkeys[left]
            monkey = right
        elif right not in remaining_monkeys:
            my_value -= monkeys[right]
            monkey = left
        else:
            print("ERROR!")
    elif op == "-":
        if left not in remaining_monkeys:
            my_value = monkeys[left] - my_value
            monkey = right
        elif right not in remaining_monkeys:
            my_value += monkeys[right]
            monkey = left
        else:
            print("ERROR!")
    elif op == "*":
        if left not in remaining_monkeys:
            my_value //= monkeys[left]
            monkey = right
        elif right not in remaining_monkeys:
            my_value //= monkeys[right]
            monkey = left
        else:
            print("ERROR!")
    elif op == "/":
        if left not in remaining_monkeys:
            my_value = monkeys[left] / my_value
            monkey = right
        elif right not in remaining_monkeys:
            my_value *= monkeys[right]
            monkey = left
        else:
            print("ERROR!")

print(my_value)