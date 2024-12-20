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
    print(INVENTORY)

def level_1(player):
    player_sprite = player.sprite
    utils.insert_newline(2)
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    items_picked_up = 0
    game_is_paused = False
    while steps_to_take > 0:
        # Hide cursor.
        print("\x1b[?25l", end="")

        # Reset steps to random number at the top of loop
        if steps_to_take == 1:
            steps_to_take = random.randrange(10, 26, 3)
            
        # Set level length and item chance of spawning
        if current_steps_taken > 10 and total_steps_taken < 76:
            if random.choice(item_chance):
                # Spawn item
                item = Item.generate_item()
                Item.spawn_item(total_steps_taken, item)
                player_input = Item.item_decision(item)
                current_steps_taken = 0
                if player_input == "e":
                    item.add_item_to_inventory(item)
                if player_input == "i":
                    game_is_paused = True
                    update_inventory = item.update_inventory()
                    inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
                    player_input = inventory_ui.inventory_decision()
                    if player_input == "d":
                        discard_item = item.discard_item()
                        if discard_item == "k":
                            inventory_ui.close_inventory(inventory_grid)
                        game_is_paused = False
                    if player_input == "i":
                        inventory_ui.close_inventory(inventory_grid)
                        player_input = Item.item_decision(item)
                        game_is_paused = False

        def handle_item_input(player_input, item):
            if player_input == "e":
                item.add_item_to_inventory(item)
            elif player_input == "i":
                update_inventory = item.update_inventory()
                inventory_grid = inventory_ui.display_inventory(update_inventory, 3, 3)
                player_input = inventory_ui.inventory_decision()
                if player_input == "d":
                    discard_item = item.discard_item()
                    if discard_item == "k":
                        inventory_ui.close_inventory(inventory_grid)



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

    
if __name__ == "__main__":
    main()
