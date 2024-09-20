# categories: tool, weapon, potion, food, magic
# names: [pick, wrench], [sword, laser], [healing, fireball, speed], [apple], [jetpack, magic_boots]
# attributes: name, category, can_equip, can_heal, can_attack, melee_pts, breaking_pts,
# effects: [repair, break], [damage], [heal, damage, speed], [heal], [fly, jump]

class Item:
    def __init__(self, name, category, effect, hit_points=0):

        # Handle Broken Items
        if name.startswith("broken_"):
            i = name.find("_") + 1
            self.repaired_name = name[i:]

        # Strings
        self.name = name
        self.category = category
        self.effect = effect

        # Handle Category
        if category == "tool":
            self.can_equip = True
            self.can_heal = False
            self.can_attack = True
            self.effect = effect
            self.strength = hit_points

        if category == "weapon":
            self.can_equip = True
            self.can_heal = False
            self.can_attack = True
            self.effect = effect
            self.strength = hit_points

        if category == "potion":
            self.can_equip = True
            self.can_heal = True
            self.can_attack = True
            self.effect = effect
            self.strength = hit_points

        if category == "food":
            self.can_equip = False
            self.can_heal = True
            self.can_attack = False
            self.effect = effect
            self.strength = hit_points

        if category == "broken":
            self.can_equip = False
            self.can_heal = False
            self.can_attack = False
            self.effect = effect
            self.strength = hit_points

        # Handle Name
        if self.name == "pick":
            self.sprite = "\x1b[1;97m‾\x1b[1;91m/\x1b[1;97m¬\x1b[0m"
        elif self.name == "wrench":
            self.sprite = "\x1b[1;94m¬\x1b[1;97mμ\x1b[0m"
        elif self.name == "sword":
            self.sprite = "\x1b[1;91m~{\x1b[1;97m=>\x1b[0m"
        elif self.name == "laser":
            self.sprite = ""
                    
"""                    
\x1b[1

‾/¬

¬μ

=¤

"""

    def tool_fix(self, broken_item):
        if self.category == "tool" and self.effect == "repair":
            broken_item.name = self.repaired_name
                        
        
        
        
        



