input_file = open('input.txt', 'r')
inputs = input_file.readlines()

def hasAdjacentSymbol(i, j):
    if (inputs[i][j] == '*'):
        return True
    return False

coords = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

gears = {}


for i in range(len(inputs)):
    inputs[i] = inputs[i].strip()
    curr = ""
    gear_pos = None
    for j in range(len(inputs[i])):
        if inputs[i][j].isdigit():
            curr += inputs[i][j]
            for x, y in coords:
                r = i + x
                c = j + y
                if (r >= 0 and r < len(inputs) and c >= 0 and c < len(inputs[i])):
                    if (hasAdjacentSymbol(r, c)):
                        gear_pos = (r, c)
        else:
            if gear_pos:
                if gear_pos in gears:
                    gears[gear_pos].append(int(curr))
                else:
                    gears[gear_pos] = [int(curr)]
            curr = ""
            gear_pos = None
    if gear_pos:
        if gear_pos in gears:
            gears[gear_pos].append(int(curr))
        else:
            gears[gear_pos] = [int(curr)]

sum = 0
for gear in gears.values():
    if len(gear) == 2:
        sum += int(gear[0]) * int(gear[1])

print(sum)

