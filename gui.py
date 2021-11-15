import tkinter as tk
import gen


class Window:
    def __init__(self):
        # Window config
        self.window = tk.Tk()
        self.window.title("Display")
        self.window.geometry("500x500")
        self.window.minsize(gen.MAX_WIDTH, gen.MAX_HEIGHT)
        self.window.maxsize(500, 500)
        self.window.config(width=500, height=500)

        # Canvas config
        self.canvas = tk.Canvas(self.window, bg="grey", width=gen.MAX_WIDTH, height=gen.MAX_HEIGHT)
        self.canvas.pack()

    def display_node(self, pos: (int, int)):
        self.canvas.create_oval(pos[0] - 5, pos[1] - 5, pos[0] + 5, pos[1] + 5, fill="black")

    def draw_line(self, pos1: (int, int), pos2: (int, int)):
        self.canvas.create_line(pos1[0], pos1[1], pos2[0], pos2[1], fill="red", width=2)

    def display_graph(self, my_graph: gen.Graph):
        nodes = my_graph.get_nodes()
        print(nodes)
        for node in nodes:
            self.display_node(node)

        for i in range(len(nodes) - 1):
            self.draw_line(nodes[i], nodes[i + 1])

    def start(self):
        self.window.mainloop()


window = Window()
seed = gen.gen_seed()
print(seed)
graph = gen.Graph(seed="f09f")
window.display_graph(graph)
window.start()
