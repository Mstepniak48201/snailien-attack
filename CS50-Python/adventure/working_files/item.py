import sys
import random
import time
import utils
from global_vars import INVENTORY, INVENTORY_DICT

# Todo: flower box input, indicate when item picked up.

class Item:
    def __init__(self, name, strength=0):
        # Handle Broken Items
        if name.startswith("broken "):
            i = name.find(" ") + 1
            self.repaired_name = name[i:]
            self.is_broken = True

        self.name = name 
        self.quantity = 1

        # Set Attributes by name
        def particle_effect(i=0):
            p1 = "\x1b[1;95m ٜ\x1b[0m"
            p2 = "\x1b[1;95m٠\x1b[0m"
            p3 = "\x1b[1;95m.\x1b[0m"
            effect_list = [p1, p2, p3]
            return effect_list

        # Use JSON instead
        if self.name == "pick":
            self.sprite = "\x1b[1;97m‾\x1b[1;91m/\x1b[1;97m¬\x1b[0m"
            self.stackable = False
            self.can_equip = True
            self.equip_location = "hand"
            self.category = "tool"
            self.durability = 6
            self.item_damage = 5
            self.attack_damage = 2
        elif self.name == "sword":
            self.sprite = "\x1b[1;91m~{\x1b[1;97m=>\x1b[0m"
            self.stackable = False
            self.can_equip = True
            self.equip_location = "hand"
            self.category = "weapon"
            self.durability = 7
            self.attack_damage = random.randrange(4, 7)
        elif self.name == "apple":
            self.sprite = "🍏"
            self.stackable = True
            self.can_consume = True
            self.consumption_type = "eat"
            self.category = "food"
            self.heal = 3
        elif self.name == "wrench":
            self.sprite = "\x1b[1;94m¬\x1b[1;97mμ\x1b[0m"
            self.stackable = False
            self.can_equip = True
            self.equip_location = "hand"
            self.category = "tool"
            self.repair = random.randrange(3, 7)
        elif self.name == "healing potion":
            self.sprite = "\x1b[1;97m⛣ \x1b[0m"
            self.stackable = True
            self.can_consume = True
            self.consumption_type = "use"
            self.category = "potion"            
            self.heal = random.randrange(2, 7)
        elif self.name == "fireball potion":
            self.sprite = "\x1b[1;93m⛣ \x1b[0m"
            self.stackable = True
            self.can_equip = True
            self.equip_location = "hand"
            self.category = "potion"
            self.attack_damage = random.randrange(5, 10)
        elif self.name == "magic boots":
            shoe1 = "\x1b[1;96m▚\x1b[0m"
            shoe2 = "\x1b[1;97m▞\x1b[0m"
            self.sprite = "\x1b[1;96m▟\x1b[1;97m◟\x1b[0m"
            self.stackable = False
            self.can_equip = True
            self.equip_location = "feet"
            self.animation = [f"{p1}{shoe1}",f"{p2}{shoe2}", f"{p3}" ]
            self.category = "magic"
            self.wearable = [True, "feet"]
            self.can_jump = True
            self.jump_chance = random.randrange(4, 15)
            self.speed = 2
        elif self.name == "laser":
            self.sprite = "\x1b[1;96m]\x1b[1;93m=\x1b[1;96m¤\x1b[0m"
            self.stackable = False
            self.can_equip = True
            self.equip_location = "hand"
            self.category = "weapon"
            self.attack_damage = random.randrange(6, 9)
        elif self.name == "speed potion":
            self.sprite = "\x1b[1;92m⛣ \x1b[0m"
            self.stackable = True
            self.can_consume = True
            self.consumption_type = "use"
            self.category = "potion"
            self.speed = 3
        elif self.name == "jetpack":
            jtpk = "\x1b[1;97m⟃⟄\x1b[0m"
            e1 = "\x1b[1;91m◦\x1b[0m"
            e2 = "\x1b[1;93m◦\x1b[0m"
            e3 = "\x1b[1;97m◦\x1b[0m"
            self.sprite = jtpk
            self.stackable = True
            self.can_equip = True
            self.equip_location = "back"
            self.use_animation = [f"{jtpk}", f"{e1}{jtpk}", f"{e2}{e1}{jtpk}", f"{e3}{e2}{e1}{jtpk}", f"{e2}{e1} {jtpk}"]
            self.category = "magic"
            self.wearable = True
            self.can_fly = True
            self.speed = 3

# Animations?
#  ٜ٠٠.

# ▟◟

    # Add __repr__ method. Best practices are to represent the data
    # visually as close to the way it is entered as possible
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    # To call repair_item():
    # new_item = broken_item.repair_item()
    def repair_item(self):
        if self.is_broken == True:
            print(f"This {self.name} is broken")
            name = self.repaired_name
        return Item(name)
    
    """
    @classmethod
    def get_rank(cls):
        # Ranks: required items to achieve rank.
        rank_1 = ["sword", "pick", "apple"]
        item_names = []
        result = []
        # Get names of inventory items.
        for item in INVENTORY:
            item_names.append(item.name)
        # Check rank against existing items.
        for name in name_list:
            if name in rank_1:
                result.append(True)
            else:
                result.append(False)
        if all(result):
    """

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
    def spawn_item(cls, total_steps_taken, item):
        sys.stdout.write(f"\r{total_steps_taken * '_'}🌀\x1b[1;92m<\x1b[0m___{item.sprite}\x1b[?25l")
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
            player_input = input(f"\nPress I to view and manage inventory, or K to return to game. ")
            utils.move_cursor_up()
            utils.erase_line()
            utils.move_cursor_up()
            return player_input
        if can_equip:
            player_input = input(f"\nPress Q to equip the {item.name} to your {item.equip_location}, or E to add to inventory. Press I to view and manage inventory, or K to return to game. ").lower()
            utils.move_cursor_up()
            utils.erase_line()
        if can_consume:
            player_input = input(f"\nPress Spacebar to {item.consumption_type}, the {item.name} now, or E to add to inventory. Press I to view and manage inventory, or K to return to game. ").lower()
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
