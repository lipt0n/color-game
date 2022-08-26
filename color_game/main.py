import curses
from color_game.color import Color
from color_game.game import Game


def main(scr: curses.window):

    # initialize game
    game = Game(max_turns=21)

    # clear screen
    scr.clear()
    curses.curs_set(0)

    height, width = scr.getmaxyx()

    # handle minimal requirements
    if height < 22:
        exit("sorry, your terminal is to small")
    if width < 54:
        exit("sorry, your terminal is to narrow")
    if curses.has_colors():
        curses.use_default_colors()
    else:
        exit("Sry, this game requires color support")

    # setup colors for game board
    curses.init_pair(Color.RED.value, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(Color.GREEN.value, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(Color.BLUE.value, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(Color.YELLOW.value, curses.COLOR_YELLOW, curses.COLOR_YELLOW)

    # and some for menu
    menu_color_mod = 10
    curses.init_pair(
        Color.RED.value + menu_color_mod, curses.COLOR_BLACK, curses.COLOR_RED
    )
    curses.init_pair(
        Color.GREEN.value + menu_color_mod, curses.COLOR_BLACK, curses.COLOR_GREEN
    )
    curses.init_pair(
        Color.BLUE.value + menu_color_mod, curses.COLOR_BLACK, curses.COLOR_BLUE
    )
    curses.init_pair(
        Color.YELLOW.value + menu_color_mod, curses.COLOR_BLACK, curses.COLOR_YELLOW
    )

    # setup game window
    begin_x = 10
    begin_y = 2
    height = 20
    width = 20
    win = curses.newwin(height, width, begin_y, begin_x)
    win.box()

    for y_row in game.map.fields:
        for field in y_row:
            win.addstr(
                field.x + 1, field.y + 1, " ", curses.color_pair(field.color.value)
            )

    # display game name
    scr.addstr(1, 15, "COLOR GAME")

    # add some controlls
    scr.addstr(5, 40, "( ) ADD RED")
    scr.addstr(7, 40, "( ) ADD GREEN")
    scr.addstr(9, 40, "( ) ADD BLUE")
    scr.addstr(11, 40, "( ) ADD YELLOW")

    scr.addstr(5, 41, "r", curses.color_pair(Color.RED.value + menu_color_mod))
    scr.addstr(7, 41, "g", curses.color_pair(Color.GREEN.value + menu_color_mod))
    scr.addstr(9, 41, "b", curses.color_pair(Color.BLUE.value + menu_color_mod))
    scr.addstr(11, 41, "y", curses.color_pair(Color.YELLOW.value + menu_color_mod))
    scr.addstr(1, 40, f"turn {game.turn}/{game.max_turns}")

    # add hint where the start is
    win.addstr(0, 0, "⬂", curses.A_BLINK)

    scr.refresh()
    win.refresh()

    while not game.is_game_over() and not game.is_game_won():
        key = win.getkey().lower()
        match key:
            case "r":
                game.set_color(Color.RED)
            case "g":
                game.set_color(Color.GREEN)
            case "b":
                game.set_color(Color.BLUE)
            case "y":
                game.set_color(Color.YELLOW)
            case _:
                pass
        # redraw
        for y_row in game.map.fields:
            for field in y_row:
                win.addstr(
                    field.x + 1, field.y + 1, " ", curses.color_pair(field.color.value)
                )
        # update current turn info
        scr.addstr(1, 40, f"turn {game.turn}/{game.max_turns}")
        scr.refresh()

    is_game_won = game.is_game_won()
    if game.is_game_over() and not is_game_won:
        scr.addstr(3, 40, "YOU LOOSE ;[", curses.A_BLINK)
    if is_game_won:
        scr.addstr(3, 40, "YEY!! YOU WIN!!!!!", curses.A_BLINK)
    scr.refresh()
    win.getkey()
    win.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
