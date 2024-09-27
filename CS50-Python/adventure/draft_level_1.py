import sys
import random
import utils
from player import Player
from item import Item 
from config import INVENTORY

def main():
    player = Player("Michael")
    level_one = level_1(INVENTORY, player)
    print(INVENTORY)

def level_1(inventory, player):
    player_sprite = player.sprite
    utils.insert_newline(2)
    steps_to_take = random.randrange(10, 26, 3)
    current_steps_taken = 0
    total_steps_taken = 0
    items_picked_up = 0
    while steps_to_take > 0:
        # Hide cursor.
        print("\x1b[?25l", end="")

        # Reset steps to random number at the top of loop
        if steps_to_take == 1:
            steps_to_take = random.randrange(10, 26, 3)
            
        # Set level lenght and item chance of spawning
        if current_steps_taken > 10 and total_steps_taken < 78:
            item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
            if random.choice(item_chance):
                # Spawn item
                item = Item.generate_item()
                Item.spawn_item(total_steps_taken, item)
                player_input = Item.item_decision(item, inventory)
                current_steps_taken = 0
                if player_input == "e":
                    INVENTORY.append(item)

        utils.move_element_forward(total_steps_taken, "_", player_sprite, 0.25)
        total_steps_taken += 1
        current_steps_taken += 1
        steps_to_take -= 1

        if total_steps_taken == 80:
            utils.show_cursor()
            return True


def pick_up_item(item):        
    item_dict = item.__dict__
    name = item_dict["name"]

    
if __name__ == "__main__":
    main()
