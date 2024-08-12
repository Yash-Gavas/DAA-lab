def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])  # Path compression
        return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal(graph):
    mst=[]
    graph.sort(key=lambda item:item[2])
    parent={}
    rank={}
    
    for u,v,_ in graph:
        parent[u]=u
        rank[u]=0
        parent[v]=v
        rank[v]=0
        
    for u,v,weight in graph:
        root_u=find(parent,u)
        root_v=find(parent,v)
        if root_u!=root_v:
            mst.append((u,v,weight))
            union(parent,rank,root_u,root_v)
            
    return mst
    
graph=[]
n=int(input("Enter the no of edges:"))
for _ in range(n):
    u,v,weight=input("Enter an edge (u v weight):").split()
    weight=int(weight)
    graph.append((u,v,weight))
    
mst=kruskal(graph)

print("Min Tree")
for u,v,weight in mst:
    print(f"Edge {u} -> {v} Weight {weight}")
