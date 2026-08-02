import time
import utils

class Flag:
    def __init__(self):
        self.pole = "▕"
        self.flag = f"\x1b[91m▶\x1b[0m"

    def run_up_the_flag(self):
        utils.move_cursor_up(3)
        space = " "
        time.sleep(0.2)
        # Erase start point flag.
        utils.overwrite_line(f"{space * 84}{self.pole}")
        utils.move_cursor_up()
        # Render flag at second point.
        utils.overwrite_line(f"{space * 84}{self.pole}{self.flag}")
        time.sleep(0.2)
        # Erase second point flag.
        utils.overwrite_line(f"{space * 84}{self.pole}{space * 2}")
        utils.move_cursor_up()
        # Render flag at third point.
        utils.overwrite_line(f"{space * 84}{self.pole}{self.flag}")
        time.sleep(1)
        utils.move_cursor_down(5)

    def render_flag_down(self): 
        utils.move_cursor_up(6)
        utils.move_cursor_right(84)
        print(self.pole)
        utils.move_cursor_right(84)
        print(self.pole)
        utils.move_cursor_right(84)
        print(f"{self.pole}{self.flag}")
