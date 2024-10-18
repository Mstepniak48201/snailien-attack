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
            item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
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
                    item_and_quantity = item.item_and_quantity_dict()
                    inventory_grid = inventory_ui.display_inventory(item_and_quantity, 3, 3)
                    player_input = inventory_ui.inventory_decision()
                    if player_input == "i":
                        inventory_ui.close_inventory(inventory_grid)
                        player_input = Item.item_decision(item)
                        game_is_paused = False

        if not game_is_paused:
            utils.move_element_forward(total_steps_taken, "_", player_sprite, 0.25)
            total_steps_taken += 1
            current_steps_taken += 1
            steps_to_take -= 1

        if total_steps_taken == 80:
            utils.show_cursor()
            item_and_quantity = item.item_and_quantity_dict()
            inventory_grid = inventory_ui.display_inventory(item_and_quantity, 3, 3)
            return True

def pick_up_item(item):        
    item_dict = item.__dict__
    name = item_dict["name"]

    
if __name__ == "__main__":
    main()
