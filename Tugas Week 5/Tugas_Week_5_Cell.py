def cell_decomposition(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    path = []

    def dfs(current):
        if current == end:
            path.append(current)
            return True
        visited.add(current)
        x, y = current

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0 and
                neighbor not in visited):
                if dfs(neighbor):
                    path.append(current)
                    return True

        return False

    dfs(start)
    return path[::-1] if end in visited else []

# Example usage:
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
start, end = (0, 0), (4, 4)
path = cell_decomposition(grid, start, end)
print("Path found:", path)
