def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if all(is_valid(r + dr, c + dc) and is_valid(r - dr, c - dc) for dr, dc in [(1, 1), (1, -1)]):
                if (grid[r - 1][c - 1] == 'M' and grid[r][c] == 'A' and grid[r + 1][c + 1] == 'S' and
                    grid[r - 1][c + 1] == 'M' and grid[r][c] == 'A' and grid[r + 1][c - 1] == 'S'):
                    count += 1
    return count

with open("input.txt") as file:
    text_input = file.read().strip().splitlines()

print(count_x_mas(text_input))
