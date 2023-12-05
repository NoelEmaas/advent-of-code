import sys

def part1(inputs):
    for input in inputs:
        input = input.strip()

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


