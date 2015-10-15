# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph

class Graph(object):
    """Necessary data and methods of a graph object."""

    def __init__(self, edge = list(), vertex_num = 0):
        self.vertex = range(1, vertex_num + 1)
        self.edge = edge
        return

    def __str__(self):
        sv = self.vertex.__str__()
        se = self.edge.__str__()
        return "Vertices: %s\nEdges: %s" % (sv, se)

mygraph = Graph([], 3)
print mygraph
