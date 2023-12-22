from ...common.input_reader import read_input

input_lines = read_input("src/2023/Day16/test.txt")

layout = []
energized = []

for i, input_line in enumerate(input_lines):
    layout.append(input_line.strip())

def move_right(row, col, beam_i):
    if col+1 < len(layout[0]):
        beams[beam_i] = (row, col+1, ">")
        if energized[row][col+1] not in "><v^":
            energized[row] = energized[row][:col+1] + ">" + energized[row][col+2:]
        else:
            if energized[row][col+1] == ">":
                beams.pop(beam_i)
            elif not energized[row][col+1].isdigit():
                energized[row] = energized[row][:col+1] + "2" + energized[row][col+2:]
    else:
        beams.pop(beam_i)

def move_left(row, col, beam_i):
    if col-1 >= 0:
        beams[beam_i] = (row, col-1, "<")
        if energized[row][col-1] not in "><v^":
            energized[row] = energized[row][:col-1] + "<" + energized[row][col:]
        else:
            if energized[row][col-1] == "<":
                beams.pop(beam_i)
            elif not energized[row][col-1].isdigit():
                energized[row] = energized[row][:col-1] + "2" + energized[row][col:]
    else:
        beams.pop(beam_i)

def move_down(row, col, beam_i):
    if row+1 < len(layout):
        beams[beam_i] = (row+1, col, "v")
        if energized[row+1][col] not in "><v^":
            energized[row+1] = energized[row+1][:col] + "v" + energized[row+1][col+1:]
        else:
            if energized[row+1][col] == "v":
                beams.pop(beam_i)
            elif not energized[row+1][col].isdigit():
                energized[row+1] = energized[row+1][:col] + "2" + energized[row+1][col+1:]
    else:
        beams.pop(beam_i)

def move_up(row, col, beam_i):
    if row-1 >= 0:
        beams[beam_i] = (row-1, col, "^")
        if energized[row-1][col] not in "><v^":
            energized[row-1] = energized[row-1][:col] + "^" + energized[row-1][col+1:]
        else:
            if energized[row-1][col] == "^":
                beams.pop(beam_i)
            elif not energized[row-1][col].isdigit():
                energized[row-1] = energized[row-1][:col] + "2" + energized[row-1][col+1:]
    else:
        beams.pop(beam_i)

max_energized_tiles = 0

for start_row in range(len(layout)):
    for start_col in [0, len(layout[0])-1]:
        start_direction = "<"
        if start_col == 0:
            start_direction = ">"
        energized = layout.copy()
        beams = [(start_row, start_col, start_direction)]
        energized[start_row] = energized[start_row][:start_col] + start_direction + energized[start_row][start_col+1:]
        prev_energized = []
        while prev_energized != energized:
            prev_energized = energized.copy()
            for beam_i in range(len(beams)-1, -1, -1):
                beam = beams[beam_i]
                row, col, direction = beam
                match layout[row][col]:
                    case ".":
                        match direction:
                            case ">":
                                move_right(row, col, beam_i)
                            case "<":
                                move_left(row, col, beam_i)
                            case "v":
                                move_down(row, col, beam_i)
                            case "^":
                                move_up(row, col, beam_i)
                    case "/":
                        match direction:
                            case ">":
                                move_up(row, col, beam_i)
                            case "<":
                                move_down(row, col, beam_i)
                            case "v":
                                move_left(row, col, beam_i)
                            case "^":
                                move_right(row, col, beam_i)
                    case "\\":
                        match direction:
                            case ">":
                                move_down(row, col, beam_i)
                            case "<":
                                move_up(row, col, beam_i)
                            case "v":
                                move_right(row, col, beam_i)
                            case "^":
                                move_left(row, col, beam_i)
                    case "|":
                        match direction:
                            case ">":
                                beams.append((row, col, "v"))
                                move_down(row, col, len(beams)-1)
                                move_up(row, col, beam_i)
                            case "<":
                                beams.append((row, col, "v"))
                                move_down(row, col, len(beams)-1)
                                move_up(row, col, beam_i)
                            case "v":
                                move_down(row, col, beam_i)
                            case "^":
                                move_up(row, col, beam_i)
                    case "-":
                        match direction:
                            case ">":
                                move_right(row, col, beam_i)
                            case "<":
                                move_left(row, col, beam_i)
                            case "v":
                                beams.append((row, col, "<"))
                                move_left(row, col, len(beams)-1)
                                move_right(row, col, beam_i)
                            case "^":
                                beams.append((row, col, "<"))
                                move_left(row, col, len(beams)-1)
                                move_right(row, col, beam_i)

        energized_tiles = 0
        for energized_row in energized:
            for space in energized_row:
                if space in "><v^" or space.isdigit():
                    energized_tiles += 1
        
        if energized_tiles > max_energized_tiles:
            max_energized_tiles = energized_tiles

for start_row in [0, len(layout)-1]:
    for start_col in range(len(layout[0])):
        start_direction = "^"
        if start_row == 0:
            start_direction = "v"
        energized = layout.copy()
        beams = [(start_row, start_col, start_direction)]
        energized[start_row] = energized[start_row][:start_col] + start_direction + energized[start_row][start_col+1:]
        prev_energized = []
        while prev_energized != energized:
            prev_energized = energized.copy()
            for beam_i in range(len(beams)-1, -1, -1):
                beam = beams[beam_i]
                row, col, direction = beam
                match layout[row][col]:
                    case ".":
                        match direction:
                            case ">":
                                move_right(row, col, beam_i)
                            case "<":
                                move_left(row, col, beam_i)
                            case "v":
                                move_down(row, col, beam_i)
                            case "^":
                                move_up(row, col, beam_i)
                    case "/":
                        match direction:
                            case ">":
                                move_up(row, col, beam_i)
                            case "<":
                                move_down(row, col, beam_i)
                            case "v":
                                move_left(row, col, beam_i)
                            case "^":
                                move_right(row, col, beam_i)
                    case "\\":
                        match direction:
                            case ">":
                                move_down(row, col, beam_i)
                            case "<":
                                move_up(row, col, beam_i)
                            case "v":
                                move_right(row, col, beam_i)
                            case "^":
                                move_left(row, col, beam_i)
                    case "|":
                        match direction:
                            case ">":
                                beams.append((row, col, "v"))
                                move_down(row, col, len(beams)-1)
                                move_up(row, col, beam_i)
                            case "<":
                                beams.append((row, col, "v"))
                                move_down(row, col, len(beams)-1)
                                move_up(row, col, beam_i)
                            case "v":
                                move_down(row, col, beam_i)
                            case "^":
                                move_up(row, col, beam_i)
                    case "-":
                        match direction:
                            case ">":
                                move_right(row, col, beam_i)
                            case "<":
                                move_left(row, col, beam_i)
                            case "v":
                                beams.append((row, col, "<"))
                                move_left(row, col, len(beams)-1)
                                move_right(row, col, beam_i)
                            case "^":
                                beams.append((row, col, "<"))
                                move_left(row, col, len(beams)-1)
                                move_right(row, col, beam_i)

        energized_tiles = 0
        for energized_row in energized:
            for space in energized_row:
                if space in "><v^" or space.isdigit():
                    energized_tiles += 1
        
        if energized_tiles > max_energized_tiles:
            max_energized_tiles = energized_tiles\

print(max_energized_tiles)