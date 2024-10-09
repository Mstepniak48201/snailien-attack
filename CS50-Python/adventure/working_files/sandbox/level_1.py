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
    player_sprite = player.sprite
    utils.insert_newline(3)
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    game_is_paused = False
    new_lines = 45
    new_line = "🟨"
    print(f"{new_lines * new_line}")
    utils.move_cursor_up(2)

    # while loop to continue gameplay on current line
    while steps_to_take > 0:
        utils.hide_cursor()

        # Reset steps to take at top of loop.
        if steps_to_take == 1:
            steps_to_take = random.randrange(10, 26, 3)

        # Determine whether an item will spawn.
        if get_item_chance(current_steps_taken, total_steps_taken):
            current_steps_taken = 0
            item = Item.generate_item()
            item.spawn_item(total_steps_taken, item)
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
            utils.move_element_forward(total_steps_taken, "_", player_sprite, 0.25)
            total_steps_taken += 1
            current_steps_taken += 1
            steps_to_take -= 1


        if total_steps_taken == 80:
            utils.show_cursor()
            update_inventory = item.update_inventory()
            inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            return True

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
    if current_steps_taken > 10 and total_steps_taken < 76:
        if random.choice(item_chance):
            return True
    return False

if __name__ == "__main__":
    main()


