def is_report_safe(levels):
    def is_increasing():
        for i in range(1, len(levels)):
            diff = levels[i] - levels[i-1]
            if diff < 1 or diff > 3:
                return False
        return True
    
    def is_decreasing():
        for i in range(1, len(levels)):
            diff = levels[i-1] - levels[i]
            if diff < 1 or diff > 3:
                return False
        return True
    
    return is_increasing() or is_decreasing()

def count_safe_reports(reports):
    return sum(1 for report in reports if is_report_safe(report))

def parse_input(input_str):
    lines = [line.strip() for line in input_str.split('\n') if line.strip()]
    
    return [list(map(int, line.split())) for line in lines]

with open('input.txt') as f:
	puzzle_input = f.read()

reports = parse_input(puzzle_input)
print(count_safe_reports(reports))