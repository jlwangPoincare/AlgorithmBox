# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph

class Graph(object):
    """
    Necessary data and methods of a graph object.
    A Graph object has attributes:
    Vertex: a list of names of vertices
    Edge: a list of tuples storing edge data
    Directed: True for directed graph, False for undirected
    """

    def __init__(self, vertex = 0, edge = list()):
        """vertex can be the number of vertices, assuming
        user don't really care the names of the vertices.
        Also vertex can be a list of vertex names.
        edge is a list of tuples. For undirected graph, use
        2-component tuples for convinience."""
        if isinstance(vertex, int):
            self.Vertex = range(1, vertex + 1)
        elif isinstance(vertex, list):
            self.Vertex = vertex[:]
        edge_type = len(edge[0])
        for each_edge in edge:
            if len(each_edge) != edge_type:
                print 'Wrong edge format!'
                return
        if edge_type == 3:
            self.Directed = True
        elif edge_type == 2:
            self.Directed = False
        else:
            print 'Wrong edge format!'
            return
        self.Edge = edge[:]
        return

    def __str__(self):
        return "Vertices: %s\nEdges: %s" % (self.Vertex.__str__(), self.Edge.__str__())

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
mygraph = Graph(3, [(1, 2, 1), (2, 1, 1), (2, 3, 2), (1, 3, 3)])
print mygraph
mygraph = Graph([1, 2, 3, 5], [(1, 2), (2, 3), (1, 3)])
print mygraph

#mygraph.add_vertex(3)
#print mygraph

#mygraph.add_vertex(4)
#print mygraph

#mygraph.add_edge((3, 4))
#print mygraph

#mygraph.delete_edge((2, 3))
#print mygraph

#mygraph.delete_vertex(1)
#print mygraph
