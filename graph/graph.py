# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph

class Graph(object):
    """
    Necessary data and methods of a graph object.
    A Graph object has attributes:
    Vertex: a list of names of vertices
    Edge: a list of tuples storing edge data
    Weight: a list corresponding to each edge's weight
    Directed: True for directed graph, False for undirected
    Weighted: True for weighted graph, False for unweighted
    """

    def __init__(self, vertex = 0, edge = list(), directed = False):
        """vertex can be the number of vertices, assuming
        user don't really care the names of the vertices.
        Also vertex can be a list of vertex names.
        edge is a list of tuples. For undirected graph, use
        2-component tuples for convinience."""
        # Do vertex
        if isinstance(vertex, int) and vertex > 0:
            self.Vertex = range(1, vertex + 1)
        elif isinstance(vertex, list):
            self.Vertex = []
            for item in vertex:
                self.add_vertex(item)
        else:
            print 'Wrong vertex format!'
            return
        # Do directed
        if isinstance(directed, bool):
            self.Directed = directed
        else:
            print 'Wrong directed format!'
            return
        # Do edge
        if isinstance(edge, list):
            edge_type = len(edge[0])
            for each_edge in edge:
                if len(each_edge) != edge_type:
                    print 'Wrong edge format: consistency!'
                    return
            if edge_type == 3:
                self.Weighted = True
                self.Weight = []
            elif edge_type == 2:
                self.Weighted = False
            else:
                print 'Wrong edge format: tuple members!'
                return
            self.Edge = []
            for item in edge:
                self.add_edge(item)
        else:
            print 'Wrong edge format: list!'
            return
        return

    def __str__(self):
        if self.Weighted:
            return "Vertices: %s\nEdges: %s\nWeights: %s" % (self.Vertex.__str__(), self.Edge.__str__(), self.Weight.__str__())
        return "Vertices: %s\nEdges: %s" % (self.Vertex.__str__(), self.Edge.__str__())

    def has_vertex(self, vertex):
        return (vertex in self.Vertex)

    def add_vertex(self, num):
        if isinstance(num, list):
            print 'Wrong adding vertex format: list!'
            return
        if self.has_vertex(num):
            print 'This vertex already exist'
            return
        self.Vertex.append(num)
        return

    def has_edge(self, edge_tuple):
        if not isinstance(edge_tuple, tuple):
            print 'Error find edge: not tuple!'
            return False
        if self.Directed:
            return (edge_tuple in self.Edge)
        #else: undirected
        return ((edge_tuple in self.Edge) or ((edge_tuple[1], edge_tuple[0]) in self.Edge))

    def add_edge(self, edge_tuple):
        if not isinstance(edge_tuple, tuple):
            print 'Wrong adding edge format: not tuple!'
            return
        if edge_tuple[0] == edge_tuple[1]:
            print 'No loop in simple graph'
            return
        if self.Weighted:
            if len(edge_tuple) != 3:
                print 'Wrong adding edge format: weighted!'
                return
            tempw = edge_tuple[2]
            edge_tuple = edge_tuple[:2]
            if self.has_edge(edge_tuple):
                print 'This edge already exist: weighted'
                return
            self.Weight.append(tempw)
        else:# unweighted
            if len(edge_tuple) != 2:
                print 'Wrong adding edge format: unweighted!'
                return
            if self.has_edge(edge_tuple):
                print 'This edge already exist: unweighted'
                return
        if self.has_vertex(edge_tuple[0]) and self.has_vertex(edge_tuple[1]):
            self.Edge.append(edge_tuple)
            return
        else:
            print 'Wrong adding edge format: nonexisting vertex!'
            return

    def delete_edge(self, edge_tuple):
        """edge_tuple should be a 2-component tuple"""
        if self.Weighted:
            if edge_tuple in self.Edge:
                ind = self.Edge.index(edge_tuple)
                del self.Weight[ind]
                del self.Edge[ind]
                return
            elif not self.Directed and ((edge_tuple[1], edge_tuple[0]) in self.Edge):
                ind = self.Edge.index((edge_tuple[1], edge_tuple[0]))
                del self.Weight[ind]
                del self.Edge[ind]
                return
            else:
                print 'Edge not found: weighted'
                return
        else:
            if edge_tuple in self.Edge:
                self.Edge.remove(edge_tuple)
                return
            elif not self.Directed and ((edge_tuple[1], edge_tuple[0]) in self.Edge):
                self.Edge.remove((edge_tuple[1], edge_tuple[0]))
                return
            else:
                print 'Edge not found: unweighted'
                return

    def delete_vertex(self, num_v):
        if self.has_vertex(num_v):
            selfedgecopy = self.Edge[:]
            self.Vertex.remove(num_v)
            for an_edge in selfedgecopy:
                if num_v == an_edge[0] or num_v == an_edge[1]:
                    self.delete_edge(an_edge)
            return
        #else: does not have this vertex
        print 'This vertex does not exist'
        return

    def get_degree(self, vertex):
        if not self.has_vertex(vertex):
            print 'vertex does not exist'
            return
        #else: has vertex
        if self.Directed:
            print 'Not designed for'
            return
        #else: not directed
        counter = 0
        for each_edge in self.Edge:
            if vertex in each_edge:
                counter += 1
        return counter

    def BFS(self, start):
        # Caution: no default value of start, must specify
        uncolored_vertex = self.Vertex[:]
        level = 0
        BFSqueue = []
        BFSqueue.append((start, level))
        BFSresult = []
        BFSresult.append((start, level))
        uncolored_vertex.remove(start)
        if self.Directed:
            #directed graph
            while len(BFSqueue) > 0:
                #print "Directed current BFS queue: ", BFSqueue
                tempvertex, templevel = BFSqueue.pop(0)
                for each_edge in self.Edge:
                    if each_edge[0] == tempvertex and each_edge[1] in uncolored_vertex:
                        anothervertex = each_edge[1]
                    else:
                        continue
                    BFSqueue.append((anothervertex, templevel + 1))
                    BFSresult.append((anothervertex, templevel + 1))
                    uncolored_vertex.remove(anothervertex)
        else:
            # undirected graph, easier to think
            while len(BFSqueue) > 0:
                #print "current BFS queue: ", BFSqueue
                tempvertex, templevel = BFSqueue.pop(0)
                for each_edge in self.Edge:
                    if each_edge[0] == tempvertex and each_edge[1] in uncolored_vertex:
                        anothervertex = each_edge[1]
                    elif each_edge[1] == tempvertex and each_edge[0] in uncolored_vertex:
                        anothervertex = each_edge[0]
                    else:
                        continue
                    BFSqueue.append((anothervertex, templevel + 1))
                    BFSresult.append((anothervertex, templevel + 1))
                    uncolored_vertex.remove(anothervertex)
        return BFSresult

    def is_connected(self):
        num_vertex = len(self.Vertex)
        if self.Directed:
            test = True
            for ind in range(num_vertex):
                BFS_tree = self.BFS(self.Vertex[ind])
                test = test and len(BFS_tree) == num_vertex
                if not test:
                    return test
            return test
        #else:
        BFS_tree = self.BFS(self.Vertex[0])
        return len(BFS_tree) == num_vertex

    def has_eulerian_cycle(self):
        if not self.is_connected():
            return False
        #else: connected
        if self.Directed:
            print 'Not designed for'
            return False
        #else: connected
        result = True
        for each_vertex in self.Vertex:
            result = result and (self.get_degree(each_vertex) % 2 == 0)
        return result

    #def print_eulerian_cycle(self):
        #if has_eulerian_cycle(self):


#mygraph = Graph(3, [(1, 2), (2, 3), (1, 3)])
#print mygraph
#mygraph = Graph(5, [(1, 2, 1), (2, 1, 1), (2, 3, 2), (3, 2, 2), (3, 4, 3), (5, 4, 5), (5, 1, 2)], directed = True)
#print mygraph
#mygraph = Graph([1, 1, 2, 3, 5, 8, 13], [(1, 2), (2, 3), (1, 3)])
#print mygraph
#mygraph = Graph([1, 2, 3, 5, 8, 13], [(1, 2), (2, 3), (1, 3), (2, 13), (13, 8), (5, 1)])
#print mygraph
mygraph = Graph(6, [(1, 2), (1, 4), (1, 6), (2, 3), (3, 4), (3, 6), (3, 1), (4, 5), (4, 6), (5, 6)])
print mygraph.BFS(5)
print mygraph.is_connected()
print mygraph.has_eulerian_cycle()

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
