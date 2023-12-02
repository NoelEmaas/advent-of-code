input_file = open('input.txt', 'r')
inputs = input_file.readlines()

total = 0
for input in inputs:
    input = input.strip()
    n = len(input)
    first = None
    last = None

    for i in range(n):
        if (input[i].isdigit() and not first):
            first = input[i]
        if (input[n - i - 1].isdigit() and not last):
            last = input[n - i - 1]
        if first and last:
            break
    
    total += int((first + last))

print(total)
        
