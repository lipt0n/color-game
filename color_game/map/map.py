import random
from typing import List
from color_game.color import Color
from color_game.map.field import Field


class Map:
    def __init__(self, width: int = 18, height: int = 18) -> None:
        # lets generate fields for the map
        self.fields: List[List[Field]] = []
        color_list = list(Color)

        for y in range(0, height):
            self.fields.append([])
            for x in range(0, width):
                color = random.choice(color_list)
                self.fields[y].append(Field(x, y, color))

        # now we set neighbors for fields
        for x in range(0, width):
            for y in range(0, height):
                neighbors: List[Field] = []
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                    if nx < 0 or ny < 0:
                        continue
                    try:
                        neighbors.append(self.fields[ny][nx])
                    except IndexError:
                        pass
                self.fields[y][x].set_neighbors(neighbors)

    def get_connected_fields_with_same_color(self) -> List[Field]:
        starting_field = self.fields[0][0]
        connected_fields = [
            starting_field,
        ]
        fields_to_check = [
            starting_field,
        ]

        for field in fields_to_check:
            for neighbor in field.get_matching_neighbors():
                if neighbor not in connected_fields:
                    connected_fields.append(neighbor)
                    fields_to_check.append(neighbor)
        return connected_fields

    def set_color_for_fields(self, fields: List[Field], color: Color):
        for f in fields:
            f.color = color
