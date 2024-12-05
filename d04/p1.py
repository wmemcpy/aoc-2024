def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(is_valid(r + i * dr, c + i * dc) and grid[r + i * dr][c + i * dc] == word[i] for i in range(len(word))):
                    count += 1
    return count

with open("input.txt") as file:
    text_input = file.read().strip().splitlines()

print(count_xmas(text_input))
