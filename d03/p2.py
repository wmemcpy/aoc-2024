import re

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def sum_enabled_mul(memory):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    state_pattern = r"(do\(\)|don't\(\))"

    combined_pattern = fr"{mul_pattern}|{state_pattern}"

    mul_enabled = True
    total = 0

    def mul(x, y):
        return x * y

    for match in re.finditer(combined_pattern, memory):
        if match.group(3):
            if match.group(3) == "do()":
                mul_enabled = True
            elif match.group(3) == "don't()":
                mul_enabled = False
        elif match.group(1) and mul_enabled: 
            x, y = int(match.group(1)), int(match.group(2))
            total += mul(x, y)
            
    return total


print(sum_enabled_mul(parse_input('input.txt')))
