import sys
import time

def insert_newline(n):
    newline = "\n"
    return print(f"{(n - 1) * newline}")

def move_element_forward(spaces, string, sprite, sleep):
    sys.stdout.write(f"\r{spaces * string}{sprite}")
    sys.stdout.flush() 
    time.sleep(float(sleep))

def hide_cursor():
    print("\x1b[?25l", end="")

def show_cursor():
    sys.stdout.write("\x1b[?25h")

def move_cursor_up(n=1):
    #ANSI escape code to move cursor up n lines
    sys.stdout.write(f"\x1b[{n}A")
    sys.stdout.flush()

def overwrite_line(text):
    # Clear line and move cursor to start.
    # \x1b is the ANSI escape sequence to take control of the terminal.
    # [ indicates that what follows will be a command for terminal control.
    # K is the Erase Line Command.
    sys.stdout.write("\x1b[K")
    sys.stdout.write("\r" + text)
    sys.stdout.flush()

def erase_line():
    sys.stdout.write("\x1b[2K\r")
    sys.stdout.flush()
