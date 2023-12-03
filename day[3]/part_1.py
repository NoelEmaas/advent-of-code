input_file = open('input.txt', 'r')
inputs = input_file.readlines()

def hasAdjacentSymbol(i, j):
    if (inputs[i][j] != '.' and not inputs[i][j].isdigit()):
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

sum = 0
for i in range(len(inputs)):
    inputs[i] = inputs[i].strip()
    curr = ""
    isvalid = False
    for j in range(len(inputs[i])):
        if inputs[i][j].isdigit():
            curr += inputs[i][j]
            for x, y in coords:
                r = i + x
                c = j + y
                if (r >= 0 and r < len(inputs) and c >= 0 and c < len(inputs[i])):
                    if (hasAdjacentSymbol(r, c)):
                        isvalid = True
        else:
            if isvalid:
                sum += int(curr)
            curr = ""
            isvalid = False
    if isvalid:
        sum += int(curr)
print(sum)

