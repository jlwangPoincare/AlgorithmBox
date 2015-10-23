# Intend to do some graph algotithm in this module
# Need first construct a class to represent a graph
import copy
import random

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

    def __init__(self, vertex = 0, edge = None, directed = False):
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
                self._n_add_vertex(item)
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
        if edge == None:
            edge = []
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
                self._n_add_edge(item)
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
        #functional, returning a new graph
        try:
            graph_new = self._n_add_vertex(num)
            return graph_new
        except:
            print 'Error'
            return self
        #if isinstance(num, list):
            #print 'Wrong adding vertex format: list!'
            #return self
        #if self.has_vertex(num):
            #print 'This vertex already exist'
            #return self
        #graph_copy = copy.deepcopy(self)
        #if len(graph_copy.Vertex) > 0:
            #print 'In deep copy during adding vertex, graph_copy.Vertex[0] is self.Vertex[0]? ', graph_copy.Vertex[0] is self.Vertex[0]
            #print graph_copy.Vertex[0]
            #print self.Vertex[0]
        #graph_copy.Vertex.append(num)
        #return graph_copy

    def _n_add_vertex(self, num):
        if isinstance(num, list):
            raise FormatError('Wrong adding vertex format: list!')
        if self.has_vertex(num):
            raise ExistenceError('This vertex already exist')
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
        #functional, returning a new graph
        try:
            graph_new = self._n_add_edge(edge_tuple)
            return graph_new
        except:
            print 'Error'
            return self

    def _n_add_edge(self, edge_tuple):
        if not isinstance(edge_tuple, tuple):
            raise FormatError('Wrong adding edge format: not tuple!')
        if edge_tuple[0] == edge_tuple[1]:
            raise LoopError('No loop in simple graph')
        #graph_copy = copy.deepcopy(self)
        #if len(graph_copy.Edge) > 0:
            #print 'In deep copy during adding edge, graph_copy.Edge[0] is self.Edge[0]? ', graph_copy.Edge[0] is self.Edge[0]
            #print graph_copy.Edge[0]
            #print self.Edge[0]
        if self.Weighted:
            if len(edge_tuple) != 3:
                raise FormatError('Wrong adding edge format: weighted!')
            tempw = edge_tuple[2]
            edge_tuple = edge_tuple[:2]
            if self.has_edge(edge_tuple):
                raise ExistenceError('This edge already exist: weighted')
            self.Weight.append(tempw)
            #graph_copy.Weight.append(tempw)
        else:# unweighted
            if len(edge_tuple) != 2:
                raise FormatError('Wrong adding edge format: unweighted!')
            if self.has_edge(edge_tuple):
                raise ExistenceError('This edge already exist: unweighted')
        if self.has_vertex(edge_tuple[0]) and self.has_vertex(edge_tuple[1]):
            self.Edge.append(edge_tuple)
            #graph_copy.Edge.append(edge_tuple)
            return
        else:
            raise ExistenceError('Wrong adding edge format: nonexisting vertex!')

    def delete_edge(self, edge_tuple):
        """edge_tuple should be a 2-component tuple"""
        graph_copy = copy.deepcopy(self)
        if self.Weighted:
            if edge_tuple in self.Edge:
                ind = self.Edge.index(edge_tuple)
                del graph_copy.Weight[ind]
                del graph_copy.Edge[ind]
                return graph_copy
            elif not self.Directed and ((edge_tuple[1], edge_tuple[0]) in self.Edge):
                ind = self.Edge.index((edge_tuple[1], edge_tuple[0]))
                del graph_copy.Weight[ind]
                del graph_copy.Edge[ind]
                return graph_copy
            else:
                print 'Edge not found: weighted'
                return self
        else:
            if edge_tuple in self.Edge:
                graph_copy.Edge.remove(edge_tuple)
                return graph_copy
            elif not self.Directed and ((edge_tuple[1], edge_tuple[0]) in self.Edge):
                graph_copy.Edge.remove((edge_tuple[1], edge_tuple[0]))
                return graph_copy
            else:
                print 'Edge not found: unweighted'
                return self

    def delete_vertex(self, num_v):
        graph_copy = copy.deepcopy(self)
        if self.has_vertex(num_v):
            #selfedgecopy = self.Edge[:]
            graph_copy.Vertex.remove(num_v)
            for an_edge in self.Edge:
                if num_v == an_edge[0] or num_v == an_edge[1]:
                    graph_copy = graph_copy.delete_edge(an_edge)
            return graph_copy
        #else: does not have this vertex
        print 'This vertex does not exist'
        return self

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

    def has_eulerian_path(self):
        if not self.is_connected():
            return False
        #else: connected
        if self.Directed:
            print 'Not designed for'
            return False
        #else: connected
        odd_counter = 0
        for each_vertex in self.Vertex:
            odd_counter += (self.get_degree(each_vertex) % 2)
        return odd_counter == 2

    def print_eulerian_cycle(self):
        if not has_eulerian_cycle(self):
            print 'No Eulerian cycle'
            return
        #else: has cycle
        graph_copy = copy.deepcopy(self)
        vertex_list = []

    def random_cycle_list(self, start):
        graph_copy = copy.deepcopy(self)
        edge_set = []
        if not self.has_vertex(start) or self.get_degree(start) < 2:
            print 'start point error'
            return edge_set
        #else: start point good
        v_from = start
        v_to = None
        while start != v_to:
            v_to = random.choice(graph_copy.get_neighbor_set(v_from))
            edge_set.append((v_from, v_to))
            graph_copy = graph_copy.delete_edge((v_from, v_to))
            v_from = v_to
        return edge_set

    def get_neighbor_set(self, vertex):
        neighbor_set = []
        if not self.has_vertex(vertex):
            print 'No vertex, no edge'
            return neighbor_set
        #else:has vertex
        if self.Directed:
            for each_edge in self.Edge:
                if vertex == each_edge[0]:
                    neighbor_set.append(each_edge[1])
        else:
            for each_edge in self.Edge:
                if vertex == each_edge[0]:
                    neighbor_set.append(each_edge[1])
                elif vertex == each_edge[1]:
                    neighbor_set.append(each_edge[0])
        return neighbor_set



#mygraph = Graph(3, [(1, 2), (2, 3), (1, 3)])
#print mygraph
#mygraph = Graph(5, [(1, 2, 1), (2, 1, 1), (2, 3, 2), (3, 2, 2), (3, 4, 3), (5, 4, 5), (5, 1, 2)], directed = True)
#print mygraph
#mygraph = Graph([1, 1, 2, 3, 5, 8, 13], [(1, 2), (2, 3), (1, 3)])
#print mygraph
#mygraph = Graph([1, 2, 3, 5, 8, 13], [(1, 2), (2, 3), (1, 3), (2, 13), (13, 8), (5, 1)])
#print mygraph
mygraph = Graph(6, [(1, 2), (1, 4), (1, 6), (2, 3), (3, 4), (3, 6), (3, 1), (4, 5), (4, 6), (5, 6)])
print mygraph
print mygraph.BFS(5)
print mygraph.is_connected()
print mygraph.has_eulerian_cycle()
print mygraph.random_cycle_list(5)

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
