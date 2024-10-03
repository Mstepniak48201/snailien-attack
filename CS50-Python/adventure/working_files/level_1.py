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


### TOMORROW'S BUG!!! PLAYER CAN ADD ITEM AS MANY TIMES AS THEY WANT!!!

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
            while game_is_paused:
                # Desired Steps:
                # Item Spawns, prompt player for decision.
                # Player Views Inventory / Inventory opens.
                # Player chooses to discard item.
                # Player chooses item to discard.
  

                player_input = Item.item_decision(item)
             
                
                handle_input(player_input, item)

                # Resume game.
                if player_input == "k":
                    game_is_paused = False

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

def handle_input(player_input, item):
    inventory_is_open = False
    if player_input == "e":
        item.add_item_to_inventory(item)
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

def get_item_chance(current_steps_taken, total_steps_taken):
    item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
    if current_steps_taken > 10 and total_steps_taken < 76:
        if random.choice(item_chance):
            return True
    return False

if __name__ == "__main__":
    main()


