def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    return sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))

def parse_input(input_str):
    lines = [line.strip() for line in input_str.split('\n') if line.strip()]
    
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    return left_list, right_list

with open('input.txt') as f:
	puzzle_input = f.read()
  
left_list, right_list = parse_input(puzzle_input)
print(calculate_total_distance(left_list, right_list))