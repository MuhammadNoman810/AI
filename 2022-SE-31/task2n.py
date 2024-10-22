
from collections import deque

def bfs_tree(graph, start, goal):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(f"Visiting: {node}")
        
        if node == goal:
            print(f"Goal '{goal}' found!")
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    print(f"Goal '{goal}' not found.")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

bfs_tree(graph, 'A', 'G')
