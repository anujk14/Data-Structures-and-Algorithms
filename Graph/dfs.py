'''
    Print DFS traversal of a graph (Directed graph)
    URL: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
'''

from collections import defaultdict, deque

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def DFS(self, src, visited):
        stack = deque()
        stack.append(src)
        while stack:
            vertex = stack.pop()

            if vertex in visited:
                continue

            print(vertex, end=" ")
            visited.append(vertex)

            for edge in self.graph[vertex]:
                self.DFS(edge, visited)




def main():
    g = DirectedGraph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, -3)
    g.add_edge(-3, -4)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    # g.add_edge(2, 0)
    # g.add_edge(2, 3)
    # g.add_edge(3, 3)

    print ("Following is Depth First Traversal"
                      " (starting from vertex 0)")
    g.DFS(0, [])
    print()

main()
