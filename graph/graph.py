# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph

class Graph(object):
    """
    Necessary data and methods of a graph object.
    A Graph object has attributes:
    Vertex: a list of names of vertices
    Edge: a list of tuples storing edge data
    Directed: True for directed graph, False for undirected
    Weighted: True for weighted graph, False for unweighted
    """

    def __init__(self, vertex = 0, edge = list(), directed = False):
        """vertex can be the number of vertices, assuming
        user don't really care the names of the vertices.
        Also vertex can be a list of vertex names.
        edge is a list of tuples. For undirected graph, use
        2-component tuples for convinience."""
        if isinstance(vertex, int) and vertex > 0:
            self.Vertex = range(1, vertex + 1)
        elif isinstance(vertex, list):
            self.Vertex = []
            for item in vertex:
                self.add_vertex(item)
        else:
            print 'Wrong vertex format!'
            return
        if isinstance(edge, list):
            edge_type = len(edge[0])
            for each_edge in edge:
                if len(each_edge) != edge_type:
                    print 'Wrong edge format: consistency!'
                    return
            if edge_type == 3:
                self.Weighted = True
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
        if isinstance(directed, bool):
            self.Directed = directed
        else:
            print 'Wrong directed format!'
            return
        return

    def __str__(self):
        return "Vertices: %s\nEdges: %s" % (self.Vertex.__str__(), self.Edge.__str__())

    def add_vertex(self, num):
        if isinstance(num, list):
            print 'Wrong adding vertex format: list!'
            return
        if num in self.Vertex:
            print 'This vertex already exist'
            return
        self.Vertex.append(num)
        return

    def add_edge(self, edge_tuple):
        if not isinstance(edge_tuple, tuple):
            print 'Wrong adding edge format: not tuple!'
            return
        if edge_tuple in self.Edge:
            print 'This edge already exist'
            return
        if edge_tuple[0] in self.Vertex and edge_tuple[1] in self.Vertex:
            self.Edge.append(edge_tuple)
        else:
            print 'Wrong adding edge format: nonexisting vertex!'
            return
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
                if num_v != an_edge[0] and num_v != an_edge[1]:
                    new_edge.append(an_edge)
            del self.Edge
            self.Edge = new_edge
            return
        print 'This vertex does not exist'
        return

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
        BFS_tree = self.BFS(self.Vertex[0])
        return len(BFS_tree) == num_vertex

        # Depending on BFS
    #def has_eulerian_cycle(self):
        #result = True
        #for 



#mygraph = Graph(3, [(1, 2), (2, 3), (1, 3)])
#print mygraph
#mygraph = Graph(3, [(1, 2, 1), (2, 1, 1), (2, 3, 2), (1, 3, 3)])
#print mygraph
mygraph = Graph([1, 1, 2, 3, 5, 8, 13], [(1, 2), (2, 3), (1, 3)])
print mygraph
mygraph = Graph([1, 2, 3, 5, 8, 13], [(1, 2), (2, 3), (1, 3), (2, 13), (13, 8), (5, 1)])
print mygraph
print mygraph.BFS(13)
print mygraph.is_connected()

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
