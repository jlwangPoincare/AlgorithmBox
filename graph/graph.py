# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph

class Graph(object):
    """
    Necessary data and methods of a graph object.
    A Graph object has attributes:
    Vertex: a list of names of vertices
    Edge: a list of tuples storing edge data
    """

    def __init__(self, vertex_num = 0, edge = list()):
        """vertex_num is the number of vertices, assuming
        user don't really care the names of the vertices.
        edge is a list of tuples. For undirected graph, use
        2-component tuples for convinience."""
        self.Vertex = range(1, vertex_num + 1)
        self.Edge = edge[:]
        return

    def __str__(self):
        sv = self.Vertex.__str__()
        se = self.Edge.__str__()
        return "Vertices: %s\nEdges: %s" % (sv, se)

    def add_vertex(self, num):
        if num in self.Vertex:
            print 'This vertex already exist'
            return
        self.Vertex.append(num)
        return

    def add_edge(self, edge_tuple):
        if edge_tuple in self.Edge:
            print 'This edge already exist'
            return
        self.Edge.append(edge_tuple)
        return

    def delete_edge(self, edge_tuple):
        if edge_tuple in self.Edge:
            self.Edge.remove(edge_tuple)
            return
        print 'This edge does not exist'
        return

    def delete_vertex(self, num_v):
        new_edge = []
        if num_v in self.Vertex:
            self.Vertex.remove(num_v)
            for an_edge in self.Edge:
                if num_v not in an_edge:
                    new_edge.append(an_edge)
            del self.Edge
            self.Edge = new_edge
            return
        print 'This vertex does not exist'
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

mygraph.delete_vertex(1)
print mygraph
