def calculate_similarity_score(left_list, right_list):
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts.get(num, 0)
    
    return similarity_score

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
print(calculate_similarity_score(left_list, right_list))