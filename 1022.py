from sys import stdin, stdout

from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        # makes the default value for all vertices an empty list
        self.edges = defaultdict(list)
        self.colors = defaultdict(set)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)
        self.colors['white'].add(value)

    def set_color(self, vertex, color):
        self.colors[color].add(vertex)
        for col in self.colors:
            if not col == color:
                self.colors[col].difference_update(self.colors[color])

    def add_edge(self, from_vertex, to_vertex, distance=None):
        if from_vertex == to_vertex: pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights) + "\n"
        string += "Colors: " + str(self.colors)
        return string


graph = Graph()
tokens = stdin.read().split('\n')
N = int(tokens[0])
for i in range(N):
    graph.add_vertex(i + 1)
    for v in tokens[i + 1].split(' ')[:-1]:
        graph.add_edge(i + 1, int(v))

result = []
while len(graph.colors['white']) > 0:
    graph.set_color(graph.colors['white'].pop(), 'grey')
    while len(graph.colors['grey']) > 0:
        currentVertex = graph.colors['grey'].pop()
        graph.colors['grey'].add(currentVertex)
        black = True
        for adj in graph.edges[currentVertex]:
            if adj not in graph.colors['black']:
                graph.set_color(adj, 'grey')
                black = False
        if black:
            graph.set_color(currentVertex, 'black')
            result.append(currentVertex)

stdout.write(' '.join(str(item) for item in list(reversed(result))))
