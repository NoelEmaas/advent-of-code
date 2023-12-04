input_file = open('input.txt', 'r')
inputs = input_file.readlines()

copy_count = {}

for input in inputs:
    card_number = int(input.split(':')[0].split(' ')[-1])
    winning_cards = set(int(x) for x in input.split(':')[1].split('|')[0].strip().split(' ') if x != '')
    my_cards = [int(x) for x in input.split('|')[1].strip().split(' ') if x != '']
    match = 0

    for card in my_cards:
        if card in winning_cards:
            match += 1
    
    for i in range(card_number + 1, card_number + match + 1):
        if i in copy_count:
            copy_count[i] += copy_count[card_number] + 1
        else:
            if card_number in copy_count:
                copy_count[i] = copy_count[card_number] + 1
            else:
                copy_count[i] = 1

card_count = 0
for i in range(1, len(inputs) + 1):
    card_count += copy_count[i] + 1 if i in copy_count else 1

print(card_count)
    
    
