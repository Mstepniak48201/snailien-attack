import sys
import random
import time
import utils
import inventory_ui
from ingame_ui import InGameUI
from player import Player
from flag import Flag
from item import Item
from global_vars import INVENTORY

def main():
    player = Player("Michael")
    level_one = level_1(player)

def level_1(player):
    player_sprite = player.sprite
    utils.insert_newline(9)
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    game_is_paused = False
    block = "🟨"
    brick = "🔲"
    stone = "\x1b[100m \x1b[0m"
    flag = Flag()

    # Render Flag
    flag.render_flag_down()

    # Render Castle
    render_castle(brick, stone)

    # Print terrain
    print(level_1_terrain(block, 45))

    # Move cursor back into gameplay position
    utils.move_cursor_up(2)

    # while loop to continue gameplay on current line
    while steps_to_take > 0:
        ingame_ui = InGameUI(total_steps_taken)
        ingame_ui.display_position(total_steps_taken)
        utils.hide_cursor()

        # Pause Game if at end of level.
        if total_steps_taken == 83:
            game_is_paused = True

        # Reset steps to take at top of loop.
        if steps_to_take == 1:
            steps_to_take = random.randrange(10, 26, 3)

        # Determine whether an item will spawn.
        if get_item_chance(current_steps_taken, total_steps_taken):
            current_steps_taken = 0
            item = Item.generate_item()
            item.spawn_item(total_steps_taken, item, player.slime_trail)
            game_is_paused = True
            can_pick_up = True
            utils.move_cursor_down(2)
            while game_is_paused:
                # Get player input.
                player_input = Item.item_decision(item, can_pick_up)
                item_picked_up = player.handle_input(player_input, item, can_pick_up)
                if item_picked_up:
                    can_pick_up = False

                # Resume game.
                if player_input == "k":
                    game_is_paused = False
                    utils.move_cursor_up(2)
                    item_picked_up = False
                    can_pick_up = True

        # Move player.
        if not game_is_paused:
            #utils.move_element_forward(total_steps_taken, player.slime_trail, player.sprite, sleep=0.25)
            handle_player_exit(total_steps_taken, player.slime_trail, player.sprite)
            total_steps_taken += 1
            current_steps_taken += 1
            steps_to_take -= 1

        # End Level
        if total_steps_taken == 83:
            flag.run_up_the_flag()
            utils.show_cursor()
            update_inventory = item.update_inventory()
            inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            return True

def render_castle(brick, stone):
    utils.move_cursor_right(80)
    print(f"{brick}{stone * 3}{brick}") 
    utils.move_cursor_right(80)
    print(f"{stone * 2}   {stone * 2}{brick}")
    utils.move_cursor_right(80)
    print(f"{stone * 2}   {stone * 2}{brick}")

def handle_player_exit(total_steps_taken, player_effect, player_sprite):
    stone = f"\x1b[100m{player_effect}\x1b[0m"
    if total_steps_taken < 78:
        utils.move_element_forward(total_steps_taken, player_effect, player_sprite, 0.25)
    elif total_steps_taken == 78:
        player_sprite = f"🌀\x1b[100;1;92m<\x1b[0m"
        utils.move_element_forward(total_steps_taken, player_effect, player_sprite, 0.25)
    elif total_steps_taken == 79:
        #player_sprite = f"\x1b[100m🌀\x1b[0m\x1b[1;92m<\x1b[0m"
        player_sprite = f"\x1b[100m{player_sprite}\x1b[0m"
        utils.move_element_forward(total_steps_taken, player_effect, player_sprite, 0.25)
    elif total_steps_taken == 80:
        player_sprite = f"{stone}{stone}{player_sprite}"
        utils.move_element_forward(total_steps_taken, player_effect, player_sprite, 0.25)
    elif total_steps_taken == 81:
        player_sprite = f"{stone}{stone}{player_effect}🌀"
        steps = int(total_steps_taken) - 1
        utils.move_element_forward(steps, player_effect, player_sprite, 0.25)
    elif total_steps_taken == 82:
        exit_sprite = f"{stone}{stone}{player_effect * 3}"
        steps = int(total_steps_taken) - 2
        utils.move_element_forward(steps, player_effect, exit_sprite, 0.75)

def level_1_terrain(block, length):
    terrain_list = []
    for _ in range(int(length)):
        terrain_list.append(block)
    return "".join(terrain_list)

def get_item_chance(current_steps_taken, total_steps_taken):
    item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
    if current_steps_taken > 10 and total_steps_taken < 72:
        if random.choice(item_chance):
            return True
    return False

if __name__ == "__main__":
    main()


