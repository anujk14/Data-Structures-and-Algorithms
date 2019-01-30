'''
    How to create a simple graph in Python(Adjacency list representation).
    URL: https://www.geeksforgeeks.org/graph-and-its-representations/
'''

class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertex_count):
        self.V = vertex_count
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        # Add node to src list
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Add node to dest list
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(0, self.V):
            print("Adjacency list for vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")


def main():
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()


main()
