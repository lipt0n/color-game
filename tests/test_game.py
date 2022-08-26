from color_game import __version__
from color_game.color import Color
from color_game.game import Game
from color_game.map.map import Map


def test_version():
    assert __version__ == "0.1.0"


def test_game_win():
    game = Game()
    game.map = Map(width=3, height=3)
    assert game.is_game_over() is False
    for _ in range(5):
        game.set_color(Color.RED)
        game.set_color(Color.GREEN)
        game.set_color(Color.BLUE)
        game.set_color(Color.YELLOW)

    # with such small map game should be won at 21 turn
    assert game.turn == 21
    assert game.is_game_over() is True
    assert game.is_game_won() is True


def test_game_loose():
    game = Game()
    assert game.is_game_over() is False
    for _ in range(20):
        game.set_color(Color.RED)

    assert game.turn == 21
    assert game.is_game_over() is True
    assert game.is_game_won() is False
