# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
def getNodes(n,l = []):
    for j in n.graph:
        l.append(j)
        getNodes(j, l)

#
#
# class Graph:
#
#     # Constructor
#     def __init__(self):
#
#         # default dictionary to store graph
#         self.graph = defaultdict(list)
#
#         # function to add an edge to graph
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#         # Function to print a BFS of graph
#
#     def BFS(self, s):
#
#         # Mark all the vertices as not visited
#         visited = [False] * (len(self.graph))
#
#         adj = [[] for i in range(100)]
#
#         # Create a queue for BFS
#         queue = []
#
#         # Mark the source node as
#         # visited and enqueue it
#         queue.append(s)
#         visited[s] = True
#
#         v = {}
#
#         while queue:
#
#             # Dequeue a vertex from
#             # queue and print it
#             s = queue.pop(0)
#             print(s)
#
#
#
#             # Get all adjacent vertices of the
#             # dequeued vertex s. If a adjacent
#             # has not been visited, then mark it
#             # visited and enqueue it
#             for i in self.graph[s]:
#                 if visited[i] == False:
#
#                     queue.append(i)
#                     visited[i] = True


class Graph:
    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")




# Driver code

import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)



# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 0)
g.addEdge(2, 5)
g.addEdge(3, 1)
g.addEdge(4, 1)
g.addEdge(4, 5)
g.addEdge(5, 2)
g.addEdge(5, 4)
g.addEdge(5, 0)
g.addEdge(5, 1)


def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")


# def show_edges(self):
#     for node in self.graph_dict:
#         for neighbour in self.graph_dict[node]:
#             print("(", node, ", ", neighbour, ")")

d = {}
def BFS(self, s):
    visited = {}
    for i in self.graph_dict:
        visited[i] = False
    queue = []
    queue.append(s)
    visited[s] = True
    while len(queue) != 0:
        s = queue.pop(0)
        for node in self.graph_dict[s]:
            if visited[node] != True:
                visited[node] = True
                d[s] = [node, s]
                queue.append(node)
        print(s, end=" ")

# print(g.show_edges())

print(BFS(g,1))
print(g.graph_dict.va)
print(d)
