input_file = open('input.txt', 'r')
inputs = input_file.readlines()

def hasAdjacentSymbol(i, j):
    if (inputs[i][j] != '.' and not inputs[i][j].isdigit()):
        return True
    return False

sum = 0
for i in range(len(inputs)):
    inputs[i] = inputs[i].strip()
    curr = ""
    isvalid = False
    for j in range(len(inputs[i])):
        if inputs[i][j].isdigit():
            curr += inputs[i][j]
            if i > 0:
                if hasAdjacentSymbol(i - 1, j):
                    isvalid = True
                if j > 0:
                    if hasAdjacentSymbol(i - 1, j - 1):
                        isvalid = True
                if j < len(inputs[i]) - 1:
                    if hasAdjacentSymbol(i - 1, j + 1):
                        isvalid = True
            if i < len(inputs) - 1:
                if hasAdjacentSymbol(i + 1, j):
                    isvalid = True
                if j > 0:
                    if (hasAdjacentSymbol(i + 1, j - 1)):
                        isvalid = True
                if j < len(inputs[i]) - 1:
                    if hasAdjacentSymbol(i + 1, j + 1):
                        isvalid = True
            if j > 0 and hasAdjacentSymbol(i, j - 1):
                isvalid = True
            if j < len(inputs[i]) - 1 and hasAdjacentSymbol(i, j + 1):
                isvalid = True
        else:
            if isvalid:
                sum += int(curr)
            curr = ""
            isvalid = False
    if isvalid:
        sum += int(curr)
print(sum)

