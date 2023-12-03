input_file = open('input.txt', 'r')
inputs = input_file.readlines()

total = 0
for input in inputs:
    input = input.strip()
    n = len(input)
    first = None
    last = None
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(n):
        if input[i].isdigit():
            first = input[i]
            break
        else:
            for j in range(3, 6):
                if (input[i:(i + j)] in words):
                    first = str(words.index(input[i:(i + j)]) + 1)
                    break
        if first:
            break

    for i in range(n - 1, -1, -1):
        if input[i].isdigit():
            last = input[i]
            break
        else:
            for j in range(3, 6):
                if (input[((i + 1) - j):(i + 1)] in words):
                    last = str(words.index(input[((i + 1) - j):(i + 1)]) + 1)
                    break
        if last:
            break 
    
    total += int((first + last))

print(total)
        
