from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)  
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

if __name__ == "__main__":
    g = Graph()
    n = int(input("Enter the number of edges: "))
    
    print("Enter edges in format 'u v' (space-separated):")
    for _ in range(n):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    
    start_vertex = int(input("Enter the starting vertex for traversal: "))

    print("\n\nBreadth-First Search (BFS) starting from vertex", start_vertex)
    g.bfs(start_vertex)
