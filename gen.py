import random

HEX_CHARS = "0123456789ABCDEF"
MAX_HEIGHT = 500
MAX_WIDTH = 200


class Graph:
    """
    This class stores the nodes in the zigzag
    """

    def __init__(self, nodes: [(int, int)]):
        self.__nodes = nodes

    def get_nodes(self):
        return self.__nodes


def get_seed() -> hex:
    return random.randint(0, 65535)


def get_values(seed):
    values = []
    num = seed
    # We are going to get each of the numbers inside of the seed
    while True:
        i = num % 0xf
        values.insert(0, HEX_CHARS[i])
        if num // 0xf == 0:
            break
        num //= 0xf  # int div to shift the hex
    return values


def generate_nodes(seed: hex):
    pass


print(get_values(get_seed()))
