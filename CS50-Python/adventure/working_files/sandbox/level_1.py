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
    utils.insert_newline(2)
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    game_is_paused = False

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
            while game_is_paused:
                # Get player input.
                check_pickup = check_can_pick_up(can_pick_up)
                player_input = Item.item_decision(item, can_pick_up)
                item_picked_up = handle_input(player_input, item, can_pick_up)
                if item_picked_up:
                    can_pick_up = False

                # Resume game.
                if player_input == "k":
                    game_is_paused = False
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

def check_can_pick_up(can_pick_up):
    if can_pick_up = False:
        print("cannot pick up")

def handle_input(player_input, item, can_pick_up):
    inventory_is_open = False
    if player_input == "i":
        inventory_is_open = True
        while inventory_is_open:
            # Display inventory
            update_inventory = item.update_inventory()
            inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            # Two possible inputs: D (discard), I (close inventory)
            inventory_decision = inventory_ui.inventory_decision()
            if inventory_decision == "d":
                discard_choice = item.discard_item()
                inventory_ui.refresh_inventory(inventory_grid)
            elif inventory_decision == "i":
                inventory_ui.close_inventory(inventory_grid)
                inventory_is_open = False
    if player_input == "e":
        if can_pick_up and not inventory_is_open:
            item.add_item_to_inventory(item)
            return True
        else:
            pass
        


"""
def handle_input(player_input, item, can_pick_up):
    inventory_is_open = False

    # Handle "e" inputs so as not to cause an error or open an extra inventory_ui
    if player_input == "e":
        if can_pick_up and not inventory_is_open:
            item.add_item_to_inventory(item)
            return True
        else:
            pass
    elif player_input == "i":
        inventory_is_open = True
        while inventory_is_open:
            # Display inventory
            update_inventory = item.update_inventory()
            inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
            # Two possible inputs: D (discard), I (close inventory)
            inventory_decision = inventory_ui.inventory_decision()
            if inventory_decision == "d":
                discard_choice = item.discard_item()
                inventory_ui.refresh_inventory(inventory_grid)
            elif inventory_decision == "i":
                inventory_ui.close_inventory(inventory_grid)
                inventory_is_open = False
"""

def get_item_chance(current_steps_taken, total_steps_taken):
    item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
    if current_steps_taken > 10 and total_steps_taken < 76:
        if random.choice(item_chance):
            return True
    return False

if __name__ == "__main__":
    main()


