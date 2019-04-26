from graph import GraphError
from graph import Directed_graph

class Console:

    def __init__(self, controller):
        self._controller = controller
        self._menu = "1. Get the number of vertices.\n" \
                     "2. Parse the set of vertices.\n" \
                     "3. Find out whether there is and edge from x to y.\n" \
                     "4. Parse the set of outbound edges of x.\n" \
                     "5. Parse the set of inbound edges of x.\n" \
                     "6. Retrieve the cost of the edge from x to y.\n" \
                     "7. Modify the cost of the edge from x to y.\n" \
                     "8. Add edge.\n" \
                     "9. Remove edge.\n" \
                     "10. Add vertex.\n" \
                     "11. Remove vertex.\n" \
                     "12. Print the in degree and the out degree.\n" \
                     "13. Print isolated vertices.\n" \
                     "14. Exit.\n" \
                     "15. Find the connected components of an undirected graph.\n" \
                     "16. Print lowest cost path between two vertices.\n"

    def run(self):
        while True:
            try:
                print(self._menu)
                choice = int(input())
                if choice == 1:
                    self._ui_print_number_of_vertices()
                elif choice == 2:
                    self._ui_print_vertices()
                elif choice == 3:
                    self._ui_check_edge()
                elif choice == 4:
                    self._ui_print_outbound_edges_of_x()
                elif choice == 5:
                    self._ui_print_inbound_edges_of_x()
                elif choice == 6:
                    self._ui_retrieve_cost_of_edge()
                elif choice == 7:
                    self._ui_modify_cost_of_edge()
                elif choice == 8:
                    self._ui_add_edge()
                elif choice == 9:
                    self._ui_remove_edge()
                elif choice == 10:
                    self._ui_add_vertex()
                elif choice == 11:
                    self._ui_remove_vertex()
                elif choice == 12:
                    self._ui_print_in_degree_and_out_degree()
                elif choice == 13:
                    self._ui_print_isolated_vertices()
                elif choice == 14:
                    return
                elif choice == 15:
                    self._ui_print_connected_components()
                elif choice == 16:
                    self.ui_print_lowest_cost_walk()
                else:
                    raise ValueError("invalid choice!")
            except ValueError as ve:
                print(ve)
            except GraphError as ge:
                print(ge)
            except TypeError as te:
                print(te)

    def _ui_print_number_of_vertices(self):
        print(self._controller.return_number_of_vertices())

    def _ui_add_edge(self):
        new_edge_x = int(input("x = "))
        new_edge_y = int(input("y = "))
        new_edge_cost = int(input("cost = "))
        self._controller.add_new_edge(new_edge_x, new_edge_y, new_edge_cost)

    def _ui_check_edge(self):
        x = int(input("x = "))
        y = int(input("y = "))
        if self._controller.check_if_edge_exists(x, y) is True:
            print("Edge exists!")
        else:
            print("Edge does not exist!")

    def _ui_add_vertex(self):
        x = int(input("x = "))
        self._controller.add_new_vertex(x)

    def _ui_remove_edge(self):
        edge_to_remove_x = int(input("x = "))
        edge_to_remove_y = int(input("y = "))
        self._controller.remove_edge(edge_to_remove_x, edge_to_remove_y)

    def _ui_print_vertices(self):
        list_of_vertices = self._controller.return_all_vertices()
        for vertex in list_of_vertices:
            print(vertex)

    def _ui_print_isolated_vertices(self):
        for x in self._controller.get_isolated_vertices():
            print(x)

    def _ui_print_in_degree_and_out_degree(self):
        x = int(input("x = "))
        print("In degree: ", end="")
        print(self._controller.get_in_degree(x))
        print("Out degree: ", end="")
        print(self._controller.get_out_degree(x))

    def _ui_print_outbound_edges_of_x(self):
        x = int(input("x = "))
        successors_of_x = self._controller.get_successors_of_x(x)
        for y in successors_of_x:
            print(y)

    def _ui_print_inbound_edges_of_x(self):
        x = int(input("x = "))
        predecessors_of_x = self._controller.get_predecessors_of_x(x)
        for y in predecessors_of_x:
            print(y)

    def _ui_retrieve_cost_of_edge(self):
        x = int(input("x = "))
        y = int(input("y = "))
        print(self._controller.retrieve_cost(x, y))

    def _ui_modify_cost_of_edge(self):
        x = int(input("x = "))
        y = int(input("y = "))
        new_cost = int(input("cost = "))
        self._controller.modify_cost(x, y, new_cost)

    def _ui_remove_vertex(self):
        x = int(input("x = "))
        self._controller.remove_vertex(x)

    def _ui_print_connected_components(self):
        connected_components = self._controller.get_connected_components()
        sub_graph_number = 1
        for sub_graph in connected_components:
            #for vertex1 in sub_graph.parse_vertices():
                #for vertex2 in sub_graph.parse_vertices():
                    #if vertex2 in self._controller.get_successors_of_x(vertex1):
                        #sub_graph.add_edge(vertex1, vertex2, 1)
            print("-------------------\n" + "Subgraph " + str(sub_graph_number) + "\n" + "-------------------")
            vertices = sub_graph.parse_vertices()
            print("vertices: ")
            for vertex in vertices:
                print(vertex)
            """else:
                print("edges: ")
                edges = []
                for vertex in vertices:
                    for neighbour in sub_graph.parse_dict_out(vertex):
                        pair = set()
                        pair.add(vertex)
                        pair.add(neighbour)
                        if pair not in edges:
                            print(str(vertex) + " " + str(neighbour))
                            edges.append(pair)
                print()"""
            sub_graph_number += 1

    def ui_print_lowest_cost_walk(self):
        start_vertex = int(input("start: "))
        end_vertex = int(input("end: "))
        pair_lowest_cost_and_path = self._controller.lowest_cost_walk(start_vertex, end_vertex)
        print("cost: " + str(pair_lowest_cost_and_path[0]))
        print("path: ")
        for vertex in pair_lowest_cost_and_path[1]:
            print(vertex)