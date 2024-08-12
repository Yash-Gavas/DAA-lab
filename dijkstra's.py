def dijkstra(graph, start):
    distances = {node: 999 for node in graph} #dictionary, distances from the start node
    distances[start] = 0

    unvisited = set(graph.keys()) #set

    while unvisited:
        current_node = min(unvisited, key=distances.get) 
        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:  
                distances[neighbor] = distance  

    return distances
    

graph = {} 
n = int(input("Enter the number of edges: "))

for _ in range(n):
    source, destination, weight = input("Enter an edge (source destination weight): ").split()
    weight = int(weight)

    if source not in graph:
        graph[source] = {}
    if destination not in graph:
        graph[destination] = {}

    graph[source][destination] = weight
    graph[destination][source] = weight

# Take user input for the starting node
start_node = input("Enter the starting node: ")
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node + ":")
for node, distance in distances.items():
    print("Node:", node, "Distance:", distance)

