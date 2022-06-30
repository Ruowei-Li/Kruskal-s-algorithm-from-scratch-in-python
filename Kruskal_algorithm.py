
import sys
from collections import defaultdict

def find(parent, i):
   if parent[i] == i:
      return i
   return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
       parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
       parent[yroot] = xroot
    else:
       parent[yroot] = xroot
       rank[xroot] += 1
 
def KruskalMST(num_nodes, graph):
    weight = 0
    i = 0
    e = 0
    graph.sort()
    parent = [i for i in range(num_nodes)]
    rank   = [0] * num_nodes
    while e < num_nodes - 1:
        w, u, v= graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
           e = e + 1
           weight += w
           union(parent, rank, x, y)
    print(weight)

def main(content) :
    graph = []
    for line in content:
        if line.startswith("n"):
            num_nodes = int(line.split(" = ")[-1])
        elif not line.startswith("#"):
            edge = [int(i) for i in line.split(" ")]
            if edge[0] < edge[1]:
               graph.append([edge[2], edge[0] - 1, edge[1] - 1])
    return num_nodes, graph
   
content = sys.stdin.read().splitlines()
#content = open("input50.txt", "r").read().splitlines()
num_nodes, graph = main(content)
KruskalMST(num_nodes, graph)

