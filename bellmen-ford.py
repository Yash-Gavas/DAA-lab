class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def bellman_ford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for i in range(1, V):
        for edge in edges:
            if dist[edge.src] != float('inf') and dist[edge.src] + edge.weight < dist[edge.dest]:
                dist[edge.dest] = dist[edge.src] + edge.weight

    for edge in edges:
        if dist[edge.src] != float('inf') and dist[edge.src] + edge.weight < dist[edge.dest]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source")
    for i in range(V):
        print(f"{i}\t\t{dist[i]}")

def main():
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    edges = []
    print("Enter the edges with source, destination, and weight:")
    for _ in range(E):
        src, dest, weight = map(int, input().split())
        edges.append(Edge(src, dest, weight))

    src = int(input("Enter the source vertex: "))
    bellman_ford(V, edges, src)

if __name__ == "__main__":
    main()
