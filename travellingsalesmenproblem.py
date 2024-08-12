from sys import maxsize 
from itertools import permutations

def travellingSalesmanProblem(graph, s, V):
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 

    min_path = maxsize 
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
        min_path = min(min_path, current_pathweight) 
    return min_path 
 
if __name__ == "__main__": 
    V = int(input("Enter the number of vertices: "))
    
    graph = []

    print("Enter the adjacency matrix (enter row-wise):")
    for i in range(V):
        row = list(map(int, input().split()))
        graph.append(row)
    
    s = 0 
    print("Minimum cost:", travellingSalesmanProblem(graph,s,V))
