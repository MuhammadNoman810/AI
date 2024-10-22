from queue import Queue

def shortest_path_in_maze(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    q = Queue()
    q.put((0, 0, 1)) 
    visited = set((0, 0))

    while not q.empty():
        r, c, dist = q.get()
        if r == rows - 1 and c == cols - 1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                q.put((nr, nc, dist + 1))
                visited.add((nr, nc))  
    
    return -1  
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]
result = shortest_path_in_maze(maze)
print("The shortest path length is:", result)
