def is_levels_consistent(levels):
    is_increasing = all(0 < levels[i] - levels[i-1] <= 3 for i in range(1, len(levels)))
    is_decreasing = all(0 < levels[i-1] - levels[i] <= 3 for i in range(1, len(levels)))

    return is_increasing or is_decreasing

def is_report_safe_with_dampener(levels):
    if is_levels_consistent(levels):
        return True
    
    for i in range(len(levels)):
        reduced_levels = levels[:i] + levels[i+1:]
        
        if is_levels_consistent(reduced_levels):
            return True
    
    return False

def parse_input(input_str):
    lines = [line.strip() for line in input_str.split('\n') if line.strip()]
    
    return [list(map(int, line.split())) for line in lines]

with open('input.txt') as f:
	puzzle_input = f.read()

reports = parse_input(puzzle_input)
print(sum(1 for report in reports if is_report_safe_with_dampener(report)))