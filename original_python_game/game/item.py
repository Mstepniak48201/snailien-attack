import sys
import random
import time
import utils
import json
from global_vars import INVENTORY, INVENTORY_DICT

# Todo: flower box input, indicate when item picked up.

with open("items.json", "r") as file:
    # json.load converts JSON to Python list of dictionaries
    item_data = json.load(file)

class Item:
    def __init__(self, name, strength=0, data=item_data):
        self.name = name 
        self.quantity = 1
        attributes = {}

        # Handle Broken Items
        if name.startswith("broken "):
            i = name.find(" ") + 1
            self.repaired_name = name[i:]
            self.is_broken = True

        # Attack damage may be handled separately, in which case the function will be written there.

        # Fill in ANSII escape characters that aren't valid JSON syntax.
        match name:
            case "pick": 
                self.sprite = "\x1b[1;97m‾\x1b[1;91m/\x1b[1;97m¬\x1b[0m"
            case "sword":
                self.sprite = "\x1b[1;91m~{\x1b[1;97m=>\x1b[0m" 
            case "apple":
                self.sprite = "🍏"
            case "wrench":
                self.sprite = "\x1b[1;94m¬\x1b[1;97mμ\x1b[0m"
            case "healing potion":
                self.sprite = "\x1b[1;97m⍙\x1b[0m"
            case "fireball potion":                 
                self.sprite = "\x1b[1;93m⍙\x1b[0m"
            case "magic boots":
                self.sprite = "\x1b[1;96m▟\x1b[1;97m◟\x1b[0m"
                self.shoe_1 = "\x1b[1;96m▚\x1b[0m"
                self.shoe_2 = "\x1b[1;97m▞\x1b[0m"
            case "laser":
                self.sprite = "\x1b[1;96m]\x1b[1;93m\x1b[1;96m¤\x1b[0m"
            case "jetpack":
                self.sprite = "\x1b[1;97m⟃⟄\x1b[0m"
                self.effect_1 = "\x1b[1;91m◦\x1b[0m"
                self.effect_2 = "\x1b[1;93m◦\x1b[0m"
                self.effect_3 = "\x1b[1;97m◦\x1b[0m"

        # Set Attributes by name
        def particle_effect(i=0):
            p1 = "\x1b[1;95m ٜ\x1b[0m"
            p2 = "\x1b[1;95m٠\x1b[0m"
            p3 = "\x1b[1;95m.\x1b[0m"
            effect_list = [p1, p2, p3]
            return effect_list
        
        # Handle attributes that depend on a random value.
        # When attribute is a random value, the JSON value will be a list in this format:
        # ["random", val_1, val_2]
        # The randrange is added to the attributes dictionary. 
        for item in data:
            if item["name"] == self.name:
                for key, value in item.items():
                    if isinstance(value, list) and value[0] == "random":
                        start = value[1]
                        end = value[2]
                        attributes[key] = random.randrange(start, end)
                    elif key != "name":
                        attributes[key] = value
                break

        # Copy attributes dictionary entries to self.
        for key, value in attributes.items():
            self.__dict__[key] = value

# Animations?
#  ٜ٠٠.

# ▟◟

    # Add __repr__ method. Best practices are to represent the data
    # visually as close to the way it is entered as possible
    def __repr__(self):
        # return f"{self.__class__.__name__}({self.__dict__})"
        attributes = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"Item({attributes})"

    # To call repair_item():
    # new_item = broken_item.repair_item()
    def repair_item(self):
        if self.is_broken == True:
            print(f"This {self.name} is broken")
            name = self.repaired_name
        return Item(name)    

    @classmethod
    def generate_item(cls, rank=0):
        # Initial 
        if rank == 0:
            items = ["sword", "pick", "apple"]
            name = random.choice(items)
            return Item(name)
        elif rank == 1:
            items = ["apple", "wrench", "healing potion"]
            name = random.choice(items)
            return Item(name)
        elif rank == 2:
            return Item("fireball potion")
        elif rank == 3:
            items = ["broken sword", "broken pick" ]
            name = random.choice(items)
            return Item(name)
        elif rank == 4:
            return Item("magic boots")
        elif rank == 5:
            return Item("apple")
        elif rank == 6:
            return Item("laser")
        elif rank == 7:
            items = ["apple", "healing potion", "speed potion"]
            name = random.choice(items)
            return Item(name)
        elif rank == 8:
            return Item("speed potion")
        elif rank == 9:
            return Item("jetpack")
        elif rank == 10:
            items = ["apple", "healing potion"]
            name = random.choice(items)
            return Item(name)

    @classmethod
    def spawn_item(cls, total_steps_taken, item, trail):
        sys.stdout.write(f"\r{total_steps_taken * trail}🌀\x1b[1;92m<\x1b[0m   {item.sprite}\x1b[?25l")
        return item

    @classmethod
    def no_item_decision(cls):
        player_input = input(f"\nThere is no item to pick up! Press I to view and manage inventory, or K to return to game. " ).lower()
        utils.move_cursor_up()
        utils.erase_line()

    @classmethod
    def item_decision(cls, item, can_pick_up, inventory=INVENTORY): 
        can_equip = getattr(item, "can_equip", False)
        can_consume = getattr(item, "can_consume", False)

        if not can_pick_up:
            player_input = input(f"\nPress I to view and manage inventory, or K to return to game. ").lower()
            if player_input not in ("i", "k"):
                utils.erase_lines(2)
                return
            else:
                utils.move_cursor_up()
                utils.erase_line()
                utils.move_cursor_up()
                return player_input

#            player_input_check = input(f"\nPress I to view and manage inventory, or K to return to game. ").lower()
#            if player_input_check == "i" or player_input_check == "k":
#                player_input = player_input_check
#            utils.move_cursor_up()
#            utils.erase_line()
#            utils.move_cursor_up()
#            return player_input
        if can_equip:
            player_input = input(f"\nPress Q to equip the {item.name} to your {item.equip_location}, or E to add to inventory. Press I to view and manage inventory, or K to return to game. ").lower()
            utils.move_cursor_up()
            utils.erase_line()
        if can_consume:
            player_input = input(f"\nPress Spacebar to {item.consumption_type} the {item.name} now, or E to add to inventory. Press I to view and manage inventory, or K to return to game. ").lower()
            utils.move_cursor_up()
            utils.erase_line()
        if player_input == "e" and len(inventory) >= 9:
            utils.move_cursor_up()
            utils.erase_line()
            player_input = input(f"\nYour inventory is full! Press D to discard the {item.name}, or I to view and manage inventory. ")

        utils.move_cursor_up()
        return player_input

    @classmethod
    def add_item_to_inventory(cls, item):
        item_name = item.name
        item_found = False
        if item.stackable:
            for existing_item in INVENTORY:
                if existing_item.name == item_name:
                    existing_item.quantity += 1
                    item_found = True
            if not item_found:
                INVENTORY.append(item)
        else:
            INVENTORY.append(item)

    @classmethod
    def discard_item(cls):
        while True:
            utils.move_cursor_up()
            utils.erase_line()
            time.sleep(0.1)
            player_input = input("Enter the item you want to discard. Press K to cancel. ").lower()
            for item in INVENTORY:
                if item.name == player_input:
                    INVENTORY.remove(item)
                    utils.move_cursor_up()
                    utils.erase_line()
                    time.sleep(0.1)
                    return player_input
            if player_input == "k":
                utils.move_cursor_up()
                utils.erase_line()
                time.sleep(0.1)
                return player_input
            else:
                utils.move_cursor_up()
                utils.erase_line()
                time.sleep(0.1)
                print(f"{player_input} is not in your inventory!")
                time.sleep(.5)

    @classmethod
    def update_inventory(cls):
        display_list = []
        for item in INVENTORY:
            name = item.name
            quantity = item.quantity
            display_list.append({name: quantity})
        return display_list
