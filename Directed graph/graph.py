from copy import deepcopy

class GraphError(Exception):
    pass

class Directed_graph:

    def __init__(self):
        '''
        Creates an empty graph .
        '''
        self._number_of_vertices = 0
        self._dict_out = {}
        self._dict_in = {}
        self._dict_cost = {}

    def add_vertex(self, x):
        '''
        Add a new vertex x.
        '''
        if x not in self.parse_vertices():
            self._dict_in[x] = []
            self._dict_out[x] = []
        else:
            raise GraphError("Vertex already exists!")

    def delete_vertex(self, x):
        if x not in self._dict_in.keys():
            raise GraphError("vertex does not exit!")
        for neighbor in self._dict_in[x]:
            self._dict_out[neighbor].remove(x)
            del self._dict_cost[(neighbor, x)]
        for neighbor in self._dict_out[x]:
            self._dict_in[neighbor].remove(x)
            del self._dict_cost[(x, neighbor)]
        del self._dict_out[x]
        del self._dict_in[x]

    def add_edge(self, x, y, cost):
        '''
        Add edge from x to y.
        '''
        if y not in self._dict_out[x]:
            self._dict_out[x].append(y)
            self._dict_in[y].append(x)
            self._dict_cost[(x,y)] = cost
        else:
            raise GraphError("Existing edge!")

    def delete_edge(self, x, y):
        '''
        Delete edge from x to y.
        '''
        if x not in self.parse_vertices() or y not in self.parse_vertices():
            raise GraphError("Missing vertex/vertices!")
        if self.is_edge(x, y) == False:
            raise GraphError("The edge does not exist!")
        else:
            self._dict_in[y].remove(x)
            self._dict_out[x].remove(y)
            del self._dict_cost[(x, y)]

    def is_edge(self, x, y):
        '''
        Checks whether there is an edge from x to y.
        '''
        if x not in self.parse_vertices() or y not in self.parse_vertices():
            raise GraphError("Missing vertex/vertices!")
        return y in self._dict_out[x]

    def parse_vertices(self):
        '''
        Returns an iterable containing all the vertices.
        '''
        return list(self._dict_out.keys())

    def parse_dict_in(self, x):
        '''
        Returns an iterable containing all the inbound neighbours of x.
        '''
        if x in self.parse_vertices():
            return list(self._dict_in[x])
        else:
            raise GraphError("missing vertex!")

    def parse_dict_out(self, x):
        '''
        Returns an iterable containing all the outbound neighbours of x.
        '''
        if x in self.parse_vertices():
            return list(self._dict_out[x])
        else:
            raise GraphError("missing vertex!")

    def get_cost(self, x, y):
        if x not in self.parse_vertices() or y not in self.parse_vertices():
            raise GraphError("Missing vertex/vertices!")
        if (x, y) not in self._dict_cost.keys():
            raise GraphError("edge does not exist!")
        else:
            return self._dict_cost[(x, y)]

    def set_cost(self, x, y, new_cost):
        if x not in self.parse_vertices() or y not in self.parse_vertices():
            raise GraphError("Missing vertex/vertices!")
        if (x, y) not in self._dict_cost.keys():
            raise GraphError("edge does not exist!")
        else:
            self._dict_cost[(x, y)] = new_cost

    def get_edges(self):
        return self._dict_cost

    def copy_graph(self):
        return deepcopy(self)
