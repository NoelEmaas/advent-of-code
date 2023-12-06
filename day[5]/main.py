import sys

def part1(inputs):
    seeds = list(map(int, inputs[0].split(':')[1].strip().split(' ')))
    curr_map = []
    for i in range(2, len(inputs)):
        input = inputs[i].strip()
        if ':' in input:
            continue
        if input == '':
            for i in range(len(seeds)):
                for curr in curr_map:
                    src_start = curr[0][1]
                    des_start = curr[0][0]
                    src_rng = curr[1]
                    if seeds[i] >= src_start and seeds[i] <= (src_start + src_rng):
                        seed_src_pos = seeds[i] - src_start
                        seeds[i] = des_start + seed_src_pos
                        break
            curr_map = []
            continue
        
        curr_input = input.split(' ')
        curr_map.append((list(map(int, curr_input[:2])), int(curr_input[-1])))
    print(min(seeds))

def part2(inputs):
    for input in inputs:
        input = input.strip()

if len(sys.argv) != 3:
    print('Usage: python3 main.py <part> <input_file>')
    exit(1)

input_file_path = sys.argv[2]
input_file = open(input_file_path, 'r')
inputs = input_file.readlines()

if sys.argv[1] == '1':
    part1(inputs)
if sys.argv[1] == '2':
    part2(inputs)


