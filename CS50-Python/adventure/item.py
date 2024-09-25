import random

class Item:
    def __init__(self, name, strength=0):
        # Handle Broken Items
        if name.startswith("broken "):
            i = name.find(" ") + 1
            self.repaired_name = name[i:]
            self.is_broken = True

        self.name = name 

        # Set Attributes by name
        def particle_effect(i=0):
            p1 = "\x1b[1;95m ٜ\x1b[0m"
            p2 = "\x1b[1;95m٠\x1b[0m"
            p3 = "\x1b[1;95m.\x1b[0m"
            effect_list = [p1, p2, p3]
            return effect_list

        if self.name == "pick":
            self.sprite = "\x1b[1;97m‾\x1b[1;91m/\x1b[1;97m¬\x1b[0m"
            self.category = "tool"
            self.durability = 6
            self.item_damage = 5
            self.attack_damage = 2
        elif self.name == "sword":
            self.sprite = "\x1b[1;91m~{\x1b[1;97m=>\x1b[0m"
            self.category = "weapon"
            self.durability = 7
            self.attack_damage = random.randrange(4, 7)
        elif self.name == "apple":
            self.sprite = "🍏"
            self.category = "food"
            self.heal = 3
        elif self.name == "wrench":
            self.sprite = "\x1b[1;94m¬\x1b[1;97mμ\x1b[0m"
            self.category = "tool"
            self.repair = random.randrange(3, 7)
        elif self.name == "healing potion":
            self.sprite = "placeholder"
            self.category = "\x1b[1;97m⛣ \x1b[0m"
            self.heal = random.randrange(2, 7)
        elif self.name == "fireball potion":
            self.sprite = "\x1b[1;93m⛣ \x1b[0m"
            self.category = "potion"
            self.attack_damage = random.randrange(5, 10)
        elif self.name == "magic boots":
            shoe1 = "\x1b[1;96m▚\x1b[0m"
            shoe2 = "\x1b[1;97m▞\x1b[0m"
            self.sprite = "\x1b[1;96m▟\x1b[1;97m◟\x1b[0m"
            self.animation = [f"{p1}{shoe1}",f"{p2}{shoe2}", f"{p3}" ]
            self.category = "magic"
            self.wearable = [True, "feet"]
            self.can_jump = True
            self.jump_chance = random.randrange(4, 15)
            self.speed = 2
        elif self.name == "laser":
            self.sprite = "\x1b[1;96m]\x1b[1;93m=\x1b[1;96m¤\x1b[0m"
            self.category = "weapon"
            self.attack_damage = random.randrange(6, 9)
        elif self.name == "speed potion":
            self.sprite = "\x1b[1;92m⛣ \x1b[0m"
            self.category = "potion"
            self.speed = 3
        elif self.name == "jetpack":
            jtpk = "\x1b[1;97m⟃⟄\x1b[0m"
            e1 = "\x1b[1;91m◦\x1b[0m"
            e2 = "\x1b[1;93m◦\x1b[0m"
            e3 = "\x1b[1;97m◦\x1b[0m"
            self.sprite = jtpk
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

    @classmethod
    def spawn_item(cls, level=1):
        # Initial 
        if level == 1:
            items = ["sword", "pick", "apple"]
            name = random.choice(items)
            return Item(name)
        elif level == 2:
            items = ["apple", "wrench", "healing potion"]
            name = random.choice(items)
            return Item(name)
        elif level == 3:
            return Item("fireball potion")
        elif level == 4:
            items = ["broken sword", "broken pick" ]
            name = random.choice(items)
            return Item(name)
        elif level == 5:
            return Item("magic boots")
        elif level == 6:
            return Item("apple")
        elif level == 7:
            return Item("laser")
        elif level == 8:
            items = ["apple", "healing potion", "speed potion"]
            name = random.choice(items)
            return Item(name)
        elif level == 9:
            return Item("speed potion")
        elif level == 10:
            return Item("jetpack")
        elif level == 11:
            items = ["apple", "healing potion"]
            name = random.choice(items)
            return Item(name)
