import sys
import random
import utils
import inventory_ui
from player import Player
from item import Item
from global_vars import INVENTORY

def main():
    player = Player("Michael")
    level_one = level_1(player)

def level_1(player):
    # The problem for updating the sprite is here, as it is outside of the loop!
    player_sprite = player.sprite
    utils.insert_newline(9)
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    game_is_paused = False
    block = "🟨"
    stone_1 = "🔲"
    stone = "\x1b[100m \x1b[0m"

    utils.move_cursor_up(3)
    utils.move_cursor_right(80)
    print(f"{stone_1}{stone * 3}{stone_1}")
    
    utils.move_cursor_right(80)
    print(f"{stone * 2}   {stone * 2}{stone_1}")

    utils.move_cursor_right(80)
    print(f"{stone * 2}   {stone * 2}{stone_1}")

    # Print terrain
    level_1_terrain = get_level_1_terrain("🟨", 45)
    display_level_1_terrain(level_1_terrain)

    # Move cursor back into gameplay position
    utils.move_cursor_up(2)

    # while loop to continue gameplay on current line
    while steps_to_take > 0:
        display_position(total_steps_taken)
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
                item_picked_up = handle_input(player_input, item, can_pick_up)
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

#            if total_steps_taken >= 82:
#                sprite_83 = f"{stone}{stone}{player.sprite}"
#                sys.stdout.write(f"\r{(total_steps_taken - 2) * player.slime_trail}{sprite_83}{sprite_83}{player.sprite}")
#                sys.stdout.flush() 
#                time.sleep(float(sleep))
#            else:
#                utils.move_element_forward(total_steps_taken, player.slime_trail, player.sprite, 0.25)
#            total_steps_taken += 1
#            current_steps_taken += 1
#            steps_to_take -= 1


        if total_steps_taken == 82:
            utils.show_cursor()
            update_inventory = item.update_inventory()
            inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            return True

def handle_player_exit(total_steps_taken, player_effect, player_sprite):
    stone = "\x1b[100m \x1b[0m"
    if total_steps_taken < 79:
        utils.move_element_forward(total_steps_taken, player_effect, player_sprite, 0.25)
    else:
        player_sprite = f"{stone}{stone}{player_sprite}"
        utils.move_element_forward(total_steps_taken, player_effect, player_sprite, 0.25)

def get_level_1_terrain(block, length):
    terrain_list = []
    for _ in range(int(length)):
        terrain_list.append(block)
    return terrain_list

def display_level_1_terrain(level_1_terrain):
    terrain = "".join(level_1_terrain)
    print(terrain)

def display_position(total_steps_taken):
    position = int(total_steps_taken)
    
    # Save current cursor position.
    print("\x1b[s", end="")

    # Counter display position.
    utils.move_cursor_up(6)

    # Print the counter and overwrite the same line
    print(f"\r{position}", end="")

    # Restore saved cursor position (back to player movement area)
    print("\x1b[u", end="")

     
    """
     ____    
    | 60 |
     ‾‾‾‾
    """

def handle_input(player_input, item, can_pick_up):
    inventory_is_open = False
    inventory_grid = None
    if player_input == "i":
        inventory_is_open = True
        while inventory_is_open:
            # At the top of the loop, create a list item to pas to .display_inventory().
            update_inventory = item.update_inventory() 
            if inventory_grid:
                inventory_ui.refresh_inventory(inventory_grid)                    
                inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            else:
                inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            inventory_decision = inventory_ui.inventory_decision()
            if inventory_decision:
                if inventory_decision == "d":
                    discard_choice = item.discard_item()
                elif inventory_decision == "i":
                    inventory_ui.close_inventory(inventory_grid)
                    inventory_is_open = False
            else:
                utils.erase_line()
                utils.move_cursor_up()

    elif player_input == "e" and can_pick_up:
        item.add_item_to_inventory(item)
        return True

def get_item_chance(current_steps_taken, total_steps_taken):
    item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
    if current_steps_taken > 10 and total_steps_taken < 72:
        if random.choice(item_chance):
            return True
    return False

if __name__ == "__main__":
    main()


