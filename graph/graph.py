# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph

class Graph(object):
    """Necessary data and methods of a graph object."""

    def __init__(self, vertex_num = 0, edge = list()):
        self.vertex = range(1, vertex_num + 1)
        self.edge = edge[:]
        return

    def __str__(self):
        sv = self.vertex.__str__()
        se = self.edge.__str__()
        return "Vertices: %s\nEdges: %s" % (sv, se)

    def add_vertex(self, num):
        if num in self.vertex:
            print 'This vertex already exist'
            return
        self.vertex.append(num)
        return

    def add_edge(self, edge_tuple):
        if edge_tuple in self.edge:
            print 'This edge already exist'
            return
        self.edge.append(edge_tuple)
        return

    def delete_edge(self, edge_tuple):
        if edge_tuple in self.edge:
            self.edge.remove(edge_tuple)
            return
        print 'This edge does not exist'
        return


mygraph = Graph(3, [(1, 2), (2, 3), (1, 3)])
print mygraph

mygraph.add_vertex(3)
print mygraph

mygraph.add_vertex(4)
print mygraph

mygraph.add_edge((3, 4))
print mygraph

mygraph.delete_edge((2, 3))
print mygraph
