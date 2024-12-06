
def move_guard(maze):
	for y, row in enumerate(maze):
		for x, cell in enumerate(row):
			if cell == '^':
				start_x, start_y = x, y
				break
		else:
			continue
		break
	
	# gauche (0), bas (1), droite (2), haut (3)
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	current_dir = 3
	
	visited = set([(start_x, start_y)])
	current_x, current_y = start_x, start_y
	
	while True:
		for _ in range(4):
			next_x = current_x + directions[current_dir][0]
			next_y = current_y + directions[current_dir][1]
			
			if (0 <= next_x < len(maze[0]) and 
				0 <= next_y < len(maze) and 
				maze[next_y][next_x] != '#'):

				current_x, current_y = next_x, next_y
				visited.add((current_x, current_y))
				break
			
			current_dir = (current_dir - 1) % 4
		else:
			break
		
		if (current_x == 0 or current_x == len(maze[0])-1 or 
			current_y == 0 or current_y == len(maze)-1):
			break
	
	return len(visited)


with open("input.txt", "r") as file:
	maze = file.read().splitlines()

visited_count = move_guard(maze)
print(move_guard(maze))