from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day12/test.txt")

total_arrangements = []

def simplify(record_text, record_num):
    done = False
    prev_record_text_overall = ""
    while record_text != prev_record_text_overall:
        prev_record_text_overall = record_text
        prev_record_text = ""
        while record_text != prev_record_text:
            prev_record_text = record_text

            while record_text[0] == ".":
                record_text = record_text[1:]

            while record_text[-1] == ".":
                record_text = record_text[:-1]

            while record_text[0] == "#":
                record_text = record_text[record_num[0]+1:]
                record_num.pop(0)
                if not record_num:
                    done = True
                    break

            if done:
                break

            while record_text[-1] == "#":
                record_text = record_text[:-1 - record_num[-1]]
                record_num.pop(-1)
                if not record_num:
                    done = True
                    break

            if done:
                break

        if done:
            break

        # only "?" on both ends
        prev_record_text = ""
        while record_text != prev_record_text:
            prev_record_text = record_text
            
            # simple case: only 1 solution
            min_spaces = 0
            for record_num_index in range(len(record_num)):
                min_spaces += record_num[record_num_index] + 1
            min_spaces -= 1
            if len(record_text) == min_spaces:
                done = True
                break

            # look from front
            while record_num[0] < len(record_text) and record_text[record_num[0]] == "#":
                record_text = record_text[1:]
            if record_text[0] != "?":
                break
            start_i = -1
            for record_text_i in range(record_num[0]):
                if record_text[record_text_i] == "#":
                    start_i = record_text_i
                    break
            
            if start_i == -1:
                # all "?"
                pass
            else:
                stop_i = start_i
                while record_text[stop_i] == "#":
                    stop_i += 1
                if stop_i - start_i == record_num[0]:
                    record_text = record_text[stop_i+1:]
                    record_num.pop(0)
                    if not record_num:
                        done = True
                        break
                else:
                    if stop_i == len(record_text):
                        done = True
                        break
                    else:
                        if record_text[stop_i] == ".":
                            record_text = record_text[stop_i+1:]
                            record_num.pop(0)
                            if not record_num:
                                done = True
                                break
                        else:
                            diff = stop_i - record_num[0]
                            if diff > 0:
                                record_text = record_text[diff:]

            # look from back
            while -1 - record_num[-1] >= 0 and record_text[-1 - record_num[-1]] == "#":
                record_text = record_text[:-1]
            if record_text[-1] != "?":
                break
            stop_i = -1
            for record_text_i in range(len(record_text) - 1, len(record_text) - record_num[-1] - 1, -1):
                if record_text[record_text_i] == "#":
                    stop_i = record_text_i + 1
                    break
            
            if stop_i == -1:
                # all "?"
                pass
            else:
                start_i = stop_i - 1
                while record_text[start_i] == "#":
                    start_i -= 1
                start_i += 1
                if stop_i - start_i == record_num[-1]:
                    record_text = record_text[:start_i-1]
                    record_num.pop(-1)
                    if not record_num:
                        done = True
                        break
                else:
                    if start_i == 0:
                        done = True
                        break
                    else:
                        if record_text[start_i-1] == ".":
                            record_text = record_text[:start_i-1]
                            record_num.pop(-1)
                            if not record_num:
                                done = True
                                break
                        else:
                            diff = len(record_text) - start_i - record_num[-1]
                            if diff > 0:
                                record_text = record_text[:-diff]

        if done:
            break

    return (done, record_text, record_num)

def get_arrangements(record_text, record_num):
    arrangements = 0
    if not record_text:
        if not record_num:
            arrangements = 1
        return arrangements
    elif not record_num:
        correct = True
        for text in record_text:
            if text == "#":
                correct = False
                break
        if correct:
            arrangements = 1
        return arrangements

    if len(record_text) < sum(record_num) + len(record_num) - 1:
        return arrangements
    
    done = False
    while not done:
        done = True
        while record_text[0] == ".":
            record_text = record_text[1:]
            if len(record_text) < sum(record_num) + len(record_num) - 1:
                return arrangements
            done = False

        while record_text[0] == "#":
            if "." in record_text[:record_num[0]]:
                return arrangements
            if len(record_text) == record_num[0] and len(record_num) == 1:
                arrangements = 1
                return arrangements
            if record_text[record_num[0]] == "#":
                return arrangements
            record_text = record_text[record_num[0]+1:]
            record_num.pop(0)
            if not record_num:
                correct = True
                for text in record_text:
                    if text == "#":
                        correct = False
                        break
                if correct:
                    arrangements = 1
                return arrangements
            if len(record_text) < sum(record_num) + len(record_num) - 1:
                return arrangements
            done = False
    
    if record_text[0] == "?":
        stop_i = 0
        while stop_i < len(record_text) and record_text[stop_i] in "?#":
            stop_i += 1
        if stop_i >= record_num[0]:
            if len(record_text) == record_num[0] and len(record_num) == 1:
                arrangements = 1
                return arrangements
            if record_text[record_num[0]] != "#":
                arrangements += get_arrangements(record_text[record_num[0]+1:], record_num[1:])
            arrangements += get_arrangements(record_text[1:], record_num)
        else:
            if "#" not in record_text[:stop_i]:
                arrangements += get_arrangements(record_text[stop_i:], record_num)
    return arrangements

for i, input_line in enumerate(input_lines):
    record_text, record_num = input_line.split()
    record_num = record_num.split(",")
    record_num = [int(record_num_i) for record_num_i in record_num]
    arrangements = 1
    done = False

    while not done:
        done, record_text, record_num = simplify(record_text, record_num)
        if not done:
            # multiple arrangements possible
            arrangements = get_arrangements(record_text, record_num)
            
            break

    total_arrangements.append(arrangements)

print(sum(total_arrangements))