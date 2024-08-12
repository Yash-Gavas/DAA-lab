from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        
        while stack:
            v = stack.pop()
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
                # Add unvisited neighbors in reverse order for correct DFS order
                for neighbour in reversed(self.graph[v]):
                    if neighbour not in visited:
                        stack.append(neighbour)

if __name__ == "__main__":
    g = Graph()
    n = int(input("Enter the number of edges: "))
    print("Enter edges in format 'u v' (space-separated):")
    for _ in range(n):
        u, v = map(int, input().split())
        g.add_edge(u, v)
    
    start_vertex = int(input("Enter the starting vertex for traversal: "))
    print("\nDepth-First Search (DFS) starting from vertex", start_vertex)
    g.dfs(start_vertex)