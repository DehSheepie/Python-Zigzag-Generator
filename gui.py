import tkinter as tk
import gen


class Window:
    def __init__(self):
        # Window config
        self.window = tk.Tk()
        self.window.title("Display")
        self.window.geometry("500x500")
        self.window.minsize(200, 500)
        self.window.maxsize(500, 500)
        self.window.config(width=500, height=500)

        # Canvas config
        self.canvas = tk.Canvas(self.window, bg="grey", width=200, height=500)
        self.canvas.pack()

    def display_node(self, pos: (int, int)):
        self.canvas.create_oval(pos[0] - 5, pos[1] - 5, pos[0] + 5, pos[1] + 5, fill="black")

    def start(self):
        self.window.mainloop()


window = Window()
window.display_node((50, 30))
window.start()
