from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in self.graph[node]:
                self.dfs(neighbour, visited)


# example usage
my_graph = Graph()

# adding edges
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)

print("Depth first traversal starting from node 1: ")
my_graph.dfs(1, set())
