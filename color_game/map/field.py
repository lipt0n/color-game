from typing import List
from color_game.color import Color


class Field(object):
    def __init__(self, x: int, y: int, color: Color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.neighbors: List["Field"] = []

    def set_neighbors(self, neighbors: List["Field"]) -> None:
        self.neighbors = neighbors

    def get_matching_neighbors(self):
        return filter(lambda n: n.color is self.color, self.neighbors)
