input_file = open('input.txt', 'r')
inputs = input_file.readlines()

import re

sum = 0
for input in inputs:
    game_num = re.search(r'Game (\d+):', input).group(1)
    colors_data = re.findall(r'(\d+) (\w+)', input)
    is_game_possible = True
    red = 0
    blue = 0
    green = 0
    for count, color in colors_data:
        if (color == 'red'):
            red = max(red, int(count))
        elif (color == 'green'):
            green = max(green, int(count))
        elif (color == 'blue'):
            blue = max(blue, int(count))
    sum += (red * green * blue)

print(sum)
