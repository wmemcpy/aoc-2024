import re

def parse_input(input_str):
    mul = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    match = re.findall(mul, input_str) 
 
    total = 0
    for m in match:
        total += int(m[0]) * int(m[1])
    
    return total


with open('input.txt', 'r') as f:
    puzzle_input = f.read()

reports = parse_input(puzzle_input)
print(reports)
