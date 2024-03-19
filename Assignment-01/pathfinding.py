from collections import deque

def is_valid_move(maze, row, col):
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= row < num_rows and 0 <= col < num_cols and maze[row][col] == 0

def bfs(maze, start, end):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        (row, col), path = queue.popleft()
        visited.add((row, col))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(maze, new_row, new_col) and (new_row, new_col) not in visited:
                if (new_row, new_col) == end:
                    return path + [(row, col), (new_row, new_col)]
                queue.append(((new_row, new_col), path + [(row, col)]))
    
    return None

def print_exploration(maze, exploration):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) in exploration:
                print('*', end=' ')
            else:
                print('#' if maze[row][col] == 1 else '.', end=' ')
        print()

# Example maze (1 represents walls, 0 represents empty spaces)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Starting position
end = (4, 4)    # Ending position

exploration = bfs(maze, start, end)

if exploration:
    print("Exploration process:")
    print_exploration(maze, exploration)
else:
    print("No path found.")
