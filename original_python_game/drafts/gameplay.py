import sys
import time
import random
from item import Item

def main():
    gameplay()

def gameplay():
    print("\n")
    print("\n")
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    items_picked_up = 0
    while steps_to_take > 0:

        if steps_to_take == 1:
            steps_to_take = random.randrange(10, 26, 3)
            
        # Hide cursor.
        print("\x1b[?25l", end="")
        if current_steps_taken > 10 and total_steps_taken < 78:
            item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
            if random.choice(item_chance):
                item = Item.generate_item()
                item_prompt = "\n Do you want to pick up the item? yes/no "
                # Abstract into function 
                # sys.stdout.write(f"\r{total_steps_taken * '_'}🌀\x1b[1;92m<\x1b[0m___🎁\x1b[?25l")
                spawn_item(total_steps_taken)
                player_input = prompt_player(item_prompt)
                current_steps_taken = 0
                if player_input == "yes":
                    items_picked_up += 1



        move_player_forward(total_steps_taken)
        total_steps_taken += 1
        current_steps_taken += 1
        steps_to_take -= 1

        if total_steps_taken == 80:
            # Show terminal cursor again
            sys.stdout.write("\x1b[?25h")
            sys.exit(f"\nYou picked up {items_picked_up} items!")

def spawn_item(total_steps_taken):
    item = Item.generate_item()
    sys.stdout.write(f"\r{total_steps_taken * '_'}🌀\x1b[1;92m<\x1b[0m___{item.sprite}\x1b[?25l")


def move_player_forward(total_steps_taken):
    sys.stdout.write(f"\r{total_steps_taken * '_'}🌀\x1b[1;92m<\x1b[0m")
    sys.stdout.flush() 
    time.sleep(0.5)
    
def prompt_player(prompt):
    player_input = input(prompt)
    move_cursor_up(1)
    overwrite_line(f"{(len(prompt) + len(player_input)) * ' '}")
    move_cursor_up(1)
    return player_input

# Move cursor up n lines
def move_cursor_up(n=1):
    #ANSI escape code to move cursor up n lines
    sys.stdout.write(f"\x1b[{n}A")
    sys.stdout.flush()

# Overwrite current line
def overwrite_line(text):
    # Clear line and move cursor to start.
    # \x1b is the ANSI escape sequence to take control of the terminal.
    # [ indicates that what follows will be a command for terminal control.
    # K is the Erase Line Command.
    sys.stdout.write("\x1b[K")
    sys.stdout.write("\r" + text)
    sys.stdout.flush()
    


if __name__ == "__main__":
    main()


"""
# Move cursor up n lines
def move_cursor_up(n=1):
    #ANSI escape code to move cursor up n lines
    sys.stdout.write(f"\x1b[{n}A")
    sys.stdout.flush()

# Function to overwrite current line
def overwrite_line(text):
    # Clear line and move cursor to start
    sys.stdout.write("\x1b[K")
    sys.stdout.write("\r" + text)
    sys.stdout.flush()

steps_to_take = random.randrange(10, 26, 3)
current_steps_taken = 0
total_steps_taken = 0
items_picked_up = 0


while steps_to_take > 0:

    if steps_to_take == 1:
        steps_to_take = random.randrange(10, 26, 3)
        

    if current_steps_taken > 10:
        item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
        if random.choice(item_chance):
            sys.stdout.write(f"\r{total_steps_taken * '_'}*__🎁")
            player_input = input("\n Do you want to pick up the item? yes/no ")
            move_cursor_up(1)
            overwrite_line(f"{(len(' Do you want to pick up the item? yes/no ') + 4) * ' '}")
            move_cursor_up(1)
            current_steps_taken = 0
            if player_input == "yes":
                items_picked_up += 1

    sys.stdout.write(f"\r{total_steps_taken * '_'}*")
    sys.stdout.flush() 
    time.sleep(0.5)
    total_steps_taken += 1
    current_steps_taken += 1
    steps_to_take -= 1

    if total_steps_taken == 80:
        sys.exit(f"\nYou picked up {items_picked_up} items!")
"""
