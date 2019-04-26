import graph
from math import inf

class Controller:

    def __init__(self, directed_graph, file_name):
        """
        Constructor for the controller class.
        :param directed_graph: object of class Directed_graph
        :param file_name: string, name of the file from which the graph will be loaded
        """
        self._directed_graph = directed_graph
        self._file_name = file_name
        self._load_from_file()

    def _load_from_file(self):
        """
        Function for loading all the vertices and all the edges of a graph.
        :return:
        """
        file = open(self._file_name, "r")
        vertices_and_edges = file.readline().strip()
        vertices_and_edges_split = vertices_and_edges.split(" ")
        number_of_vertices = int(vertices_and_edges_split[0])
        number_of_edges = int(vertices_and_edges_split[1])
        for vertex in range(0, number_of_vertices):
            self._directed_graph.add_vertex(vertex)
        for index in range(0, number_of_edges):
            line = file.readline().strip()
            line_split = line.split(" ")
            x = int(line_split[0])
            y = int(line_split[1])
            cost = int(line_split[2])
            self._directed_graph.add_edge(x, y, cost)
        file.close()

    def return_all_vertices(self):
        """
        Function for returning an iterable containing all the vertices of the graph.
        :return:
        """
        list_of_vertices = self._directed_graph.parse_vertices()
        return list_of_vertices

    def return_number_of_vertices(self):
        """
        Function for returning the total number of vertices,
        :return:
        """
        return len(self._directed_graph.parse_vertices())

    def add_new_edge(self, new_edge_x, new_edge_y, new_edge_cost):
        """
        Function for adding a new edge.
        :param new_edge_x: beginning vertex, integer
        :param new_edge_y: ending vertex, integer
        :param new_edge_cost: cost of the edge, integer
        :return:
        """
        self._directed_graph.add_edge(new_edge_x, new_edge_y, new_edge_cost)

    def check_if_edge_exists(self, x, y):
        """
        Function for checking whether the graph contains an edge having the starting vertex x and the ending vertex y.
        :param x: vertex, integer
        :param y: vertex, integer
        :return:
        """
        return self._directed_graph.is_edge(x, y)

    def add_new_vertex(self, x):
        """
        Function for adding a new vertex.
        :param x: vertex, integer
        :return:
        """
        self._directed_graph.add_vertex(x)

    def remove_edge(self, x, y):
        """
        Function for deleting an edge having the starting vertex x and the ending vertex y.
        :param x: vertex, integer
        :param y: vertex, integer
        :return:
        """
        self._directed_graph.delete_edge(x, y)

    def get_isolated_vertices(self):
        vertices = self.return_all_vertices()
        list_of_isolated_vertices = []
        for vertex in vertices:
            if len(self._directed_graph.parse_dict_in(vertex)) == 0 and len(self._directed_graph.parse_dict_out(vertex)) == 0:
                list_of_isolated_vertices.append(vertex)
        return list_of_isolated_vertices

    def get_in_degree(self, x):
        return len(self._directed_graph.parse_dict_in(x))

    def get_out_degree(self, x):
        return len(self._directed_graph.parse_dict_out(x))

    def get_successors_of_x(self, x):
        return self._directed_graph.parse_dict_out(x)

    def get_predecessors_of_x(self, x):
        return self._directed_graph.parse_dict_in(x)

    def retrieve_cost(self, x, y):
        return self._directed_graph.get_cost(x, y)

    def modify_cost(self, x, y, new_cost):
        self._directed_graph.set_cost(x, y, new_cost)

    def remove_vertex(self, x):
        self._directed_graph.delete_vertex(x)

    def get_connected_components(self):
        connected_components = []
        for vertex in self._directed_graph.parse_vertices():
            if len(connected_components) == 0:
                queue = []
                visited = set()
                queue.append(vertex)
                visited.add(vertex)
                sub_graph = graph.Directed_graph()
                sub_graph.add_vertex(vertex)
                while not len(queue) is 0:
                    x = queue.pop(0)
                    for y in self._directed_graph.parse_dict_out(x):
                        if y not in visited:
                            visited.add(y)
                            queue.append(y)
                            sub_graph.add_vertex(y)
                        if x is not y:
                            sub_graph.add_edge(x, y, 1)
                    for y in self._directed_graph.parse_dict_in(x):
                        if y not in visited:
                            visited.add(y)
                            queue.append(y)
                            sub_graph.add_vertex(y)
                connected_components.append(sub_graph)

            else:
                indicator = True
                for sub_graph in connected_components:
                    if vertex in sub_graph.parse_vertices():
                        indicator = False
                        break
                if indicator is True:
                    queue = []
                    visited = set()
                    queue.append(vertex)
                    visited.add(vertex)
                    sub_graph = graph.Directed_graph()
                    sub_graph.add_vertex(vertex)
                    while not len(queue) is 0:
                        x = queue.pop(0)
                        for y in self._directed_graph.parse_dict_out(x):
                            if y not in visited:
                                visited.add(y)
                                queue.append(y)
                                sub_graph.add_vertex(y)
                            if x is not y:
                                sub_graph.add_edge(x, y, 1)
                        for y in self._directed_graph.parse_dict_in(x):
                            if y not in visited:
                                visited.add(y)
                                queue.append(y)
                                sub_graph.add_vertex(y)
                    connected_components.append(sub_graph)

        return connected_components

    def lowest_cost_walk(self, start_vertex, end_vertex):
        distance = {}
        predecessor = {}
        vertices = list(self.return_all_vertices())
        edges_with_costs = self._directed_graph.get_edges()

        """
        Initialise distance dict and predecessor dict for the graph
        """
        for vertex in vertices:
            if vertex is start_vertex:
                distance[vertex] = 0
            else:
                distance[vertex] = inf
            predecessor[vertex] = None

        """
        Relax edges
        """
        changed = True
        #steps = 0
        #for i in range(1, len(vertices)-1):
        while changed is True:
            #steps += 1
            changed = False
            for edge in edges_with_costs.keys():
                if distance[edge[0]] + edges_with_costs[edge] < distance[edge[1]]:
                    distance[edge[1]] = distance[edge[0]] + edges_with_costs[edge]
                    predecessor[edge[1]] = edge[0]
                    changed = True

        """
        Check for negative cost cycles
        """
        for edge in edges_with_costs.keys():
            if distance[edge[0]] + edges_with_costs[edge] < distance[edge[1]]:
                raise graph.GraphError("negative cost cycle accesible from starting vertex!")

        """
        Build the list containing the vertices forming the path we are looking for
        """
        walk = []
        current_vertex = predecessor[end_vertex]
        walk.append(end_vertex)
        if(current_vertex is None):
            raise graph.GraphError("No walk between these vertices!")
        while(current_vertex != start_vertex):
            walk.append(current_vertex)
            current_vertex = predecessor[current_vertex]
        walk.append(start_vertex)


        walk.reverse()
        #print("steps: " + str(steps))
        return (distance[end_vertex], list(walk))
