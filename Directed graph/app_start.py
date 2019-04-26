from ui import Console
from controller import Controller
from graph import Directed_graph

file_name = "graph100k.txt"

directed_graph = Directed_graph()
controller = Controller(directed_graph, file_name)
console = Console(controller)
console.run()
