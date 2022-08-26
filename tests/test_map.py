from color_game.map.map import Map


def test_map():
    map = Map(width=4, height=5)
    assert len(map.fields) == 5
    assert len(map.fields[0]) == 4
