
from queue import Queue
def graph1():
    dict = {0:[1,4],
            1:[0,2,3,4],
            2:[1,3],
            3:[2,4,1],
            4:[0,1,3]}
    print(dict)




graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': [],
    'E': ['G', 'C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}



def bfs(graph, start, goal):
    visited = set()  
    q = Queue() 
    q.put(start)

    while not q.empty():
        node = q.get() 
        print(f"Visiting: {node}")

        if node == goal:  
            print(f"Goal {goal} found!")
            return

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.put(neighbor)


start_node = 'A'
goal_node = 'L' 
bfs(graph, start_node, goal_node)
graph1()
