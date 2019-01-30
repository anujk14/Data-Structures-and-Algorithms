'''
    Print BFS traversal of a graph (Directed graph)
    URL: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
'''

from collections import defaultdict, deque

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def BFS(self, src):
        visited = []

        queue = deque()
        queue.append(src)

        while queue:
            vertex = queue.popleft()

            if vertex in visited:
                continue

            print(vertex, end=" ")
            queue.extend(self.graph[vertex])
            visited.append(vertex)


def main():
    g = DirectedGraph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 0)
    g.add_edge(4, 1)

    print ("Following is Breadth First Traversal"
                      " (starting from vertex 0)")
    g.BFS(0)
    print()

main()
