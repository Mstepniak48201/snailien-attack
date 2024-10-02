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
            player_input = Item.item_decision(item)
            inventory_action = inventory_ui.inventory_decision(player_input)
            

        # Move player.
        if not game_is_paused:
            utils.move_element_forward(total_steps_taken, "_", player_sprite, 0.25)
            total_steps_taken += 1
            current_steps_taken += 1
            steps_to_take -= 1

        if total_steps_taken == 80:
            utils.show_cursor()
            return True

def get_item_chance(current_steps_taken, total_steps_taken):
    item_chance = [0, 0, 0, 0, 0, 0, 0, 0, True]
    if current_steps_taken > 10 and total_steps_taken < 76:
        if random.choice(item_chance):
            print(f"current steps taken: {current_steps_taken}, total steps taken: {total_steps_taken}")
            return True
    return False

if __name__ == "__main__":
    main()


