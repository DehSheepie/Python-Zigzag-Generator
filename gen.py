import random

MAX_HEIGHT = 500
MAX_WIDTH = 200


def gen_seed() -> str:
    return f"{hex(random.randint(0, 0xffff))[2:]:0>4}"


class Graph:
    """
    Class for the list of nodes in the zigzag
    """

    HEX = "0123456789abcdef"

    def __init__(self, seed: str = "ffff", x_nodes=5, y_nodes=5):
        self.__seed = seed
        self.__nodes = []
        self.x_nodes = x_nodes
        self.y_nodes = y_nodes
        self.gen_graph()

    def get_value(self, index, count):
        num = Graph.HEX.index(self.__seed[index])

        return ((num * count) % 0xf) + 1

    def get_nodes(self):
        return self.__nodes

    def gen_graph(self) -> [(int, int)]:
        x_seg_size = MAX_WIDTH // self.x_nodes
        y_seg_size = MAX_HEIGHT // self.y_nodes
        y = MAX_HEIGHT
        x= MAX_WIDTH//2
        while True:
            self.__nodes.append((x, y))
            x = random.randint(0, self.x_nodes) * x_seg_size
            if y == 0:
                break
            y -= y_seg_size
            if y < 0:
                y = 0
