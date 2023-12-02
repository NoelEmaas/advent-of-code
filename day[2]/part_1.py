input_file = open('input.txt', 'r')
inputs = input_file.readlines()

import re

sum = 0
for input in inputs:
    game_num = re.search(r'Game (\d+):', input).group(1)
    colors_data = re.findall(r'(\d+) (\w+)', input)
    is_game_possible = True
    for count, color in colors_data:
        if (color == 'red' and int(count) > 12):
            is_game_possible = False
            break
        elif (color == 'green' and int(count) > 13):
            is_game_possible = False
            break
        elif (color == 'blue' and int(count) > 14):
            is_game_possible = False
            break
    if (is_game_possible):
        sum += int(game_num)    

print(sum)
