import inventory_ui
import utils

class Player:
    def __init__(self, name):
        self.name = name
        self.sprite = "🌀\x1b[1;92m<\x1b[0m"
        self.counter = 0
        self.slime_trail = "\x1b[1;92m_\x1b[0m"

    def update_sprite(self, counter):
        self.counter = counter
        if self.counter > 75 and self.counter < 80:
            self.sprite = "🟢🌀\x1b[1;92m<\x1b[0m"
        else:
            self.sprite = "🌀\x1b[1;92m<\x1b[0m"


    def handle_input(self, player_input, item, can_pick_up):
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
        
            
