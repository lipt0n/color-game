from color_game.color import Color
from color_game.map.map import Map


class Game:
    def __init__(self, max_turns: int = 21) -> None:
        self.turn = 1
        self.map = Map()
        self.max_turns = max_turns

    def is_game_over(self):
        if self.turn >= self.max_turns:
            return True

        return False

    def is_game_won(self):
        color = self.map.fields[0][0].color
        for y_row in self.map.fields:
            for field in y_row:
                if field.color is not color:
                    return False
        return True

    def set_color(self, color: Color):
        fields = self.map.get_connected_fields_with_same_color()
        self.map.set_color_for_fields(fields, color)
        self.turn += 1
