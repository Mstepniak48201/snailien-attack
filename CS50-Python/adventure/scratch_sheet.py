import sys
import time
import random

# Set Attributes by name
"""
steps = 10
i = 0
p1 = "\x1b[1;95m ٜ\x1b[0m"
p2 = "\x1b[1;95m٠\x1b[0m"
p3 = "\x1b[1;95m.\x1b[0m"
effect_list = [p1, p2, p3]
"""

# Take 1st step
# Print shoe_1
# Print p1

# Take 2nd step
# Print shoe_2
# Print p2

# Take 3rd step
# Print shoe_1
# Print p3

# Take 4th step
# Print shoe_2
#Print p1

steps = 10

def print_shoes(steps):
    steps_left = int(steps)
    particle_counter = 1
    shoe_counter = 0
    p1 = "\x1b[1;95m ٜ\x1b[0m"
    p2 = "\x1b[1;95m٠\x1b[0m"
    p3 = "\x1b[1;95m.\x1b[0m"
    effect_list = [p1, p2, p3]

    while steps_left > 0:
        print(f"steps left: {steps_left}, particle counter; {particle_counter}, shoe counter: {shoe_counter}")
        if particle_counter < len(effect_list):
            particle_counter += 1
        else:
            particle_counter = 1

        if shoe_counter < 1:
            shoe_counter += 1
        else:
            shoe_counter = 0

        steps_left -= 1
    return "All done!"

print("\x1b[1;95m ٜ\x1b[0m")
print("\x1b[1;95m٠\x1b[0m")
print("\x1b[1;95m.\x1b[0m")


# print_shoes(steps)
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

# Print a line and then overwrite it.
print("Line 1: Hello World!")
print("Line 2: Waiting...")

# Delay before overwriting
time.sleep(2)

move_cursor_up(1)

# Call move cursor function
overwrite_line("Line 2: Overwritten!")

# Move cursor back down for further input
print("\nLine 3: Done!")

"""

"""
for i in range(10):
    sys.stdout.write(f"\rCounting: {i}")
    sys.stdout.flush()
    time.sleep(1)
"""

"""
steps_to_take = 10
steps_taken = 0

while steps_to_take > 0:
    sys.stdout.write(f"\r{steps_taken * '_'}*")
    sys.stdout.flush() 
    time.sleep(0.5)
    steps_taken += 1
    steps_to_take -= 1
print("\ncomplete!")
"""
"""
# Generate random number of steps to take.
# Once I have how many steps I want to take, I am taking n steps.
# For every x number of steps, I want there to be a chance of an item spawning.
# For every y number of steps, I want there to be a chance of an enemy spawning.
# For every z number of steps, I want there to be a chance of an obstacle spawning.

# Write if statement to reset when steps_to_take = 1

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

# Print a line and then overwrite it.
"""
print("Line 1: Hello World!")
print("Line 2: Waiting...")

# Delay before overwriting
time.sleep(2)

move_cursor_up(1)

# Call move cursor function
overwrite_line("Line 2: Overwritten!")

# Move cursor back down for further input
print("\nLine 3: Done!")
"""



