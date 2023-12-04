input_file = open('input.txt', 'r')
inputs = input_file.readlines()

points = 0

for input in inputs:
    winning_cards = set(int(x) for x in input.split(':')[1].split('|')[0].strip().split(' ') if x != '')
    my_cards = [int(x) for x in input.split('|')[1].strip().split(' ') if x != '']
    
    curr = 0
    for card in my_cards:
        if card in winning_cards:
            curr = curr * 2 if curr != 0 else 1

    points += curr

print(points)

    
