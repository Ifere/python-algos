from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                queue = deque([(row, col)])
                while queue:
                    _row, _col = queue.popleft()

                    for i_row, j_col in [_row + 1, _col], [_row - 1, _col], [_row, _col + 1], [_row, _col - 1]:
                        if 0 <= i_row < len(grid) and 0 <= j_col < len(grid[0]) and grid[i_row][j_col] == '1':
                            grid[i_row][j_col] = '#'
                            queue.append((i_row, j_col))
                count += 1
    return count