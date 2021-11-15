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

    def __init__(self, seed: str = "ffff", density=5, zagginess=5):
        self.__seed = seed
        self.__nodes = []
        self.__density = density
        self.__zagginess = zagginess
        self.gen_graph()

    def get_value(self, index, count):
        num = Graph.HEX.index(self.__seed[index]) + 1

        return ((num * count) % 0xf) + 1

    def get_nodes(self):
        return self.__nodes

    def gen_graph(self) -> [(int, int)]:
        x = MAX_WIDTH // 2
        y = MAX_HEIGHT
        y_seg = MAX_HEIGHT // self.__density  # segment size
        y_variance = (y_seg // 0xf) + 1  # prevent 0 values
        x_seg = MAX_WIDTH // self.__zagginess  # segment size
        x_variance = (x_seg // 0xf) + 1
        counter = 1
        flip = False
        while True:
            if y == 0:
                break
            y -= y_variance
            if y < 0:
                y = 0
            if flip:
                x -= x_seg
            else:
                x += x_seg
            if x > MAX_WIDTH - 20 or x < 20:
                flip = not flip
            self.__nodes.append((x, y))
