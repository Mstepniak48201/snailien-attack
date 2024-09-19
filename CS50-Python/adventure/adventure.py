from grid import display_inventory

# Create Player class.
# Player has name, health
class Player:
    def __init__(self, name, health=20):
        self.name = name
        self.health = health

# Sword
# Apple
# Magic Shoes
# Healing Potion
class Items:
    def __init__(self):
        self.sword = False
        self.apple = 0
        self.magic_shoes = False
        self.healing_potion = 0


    
        

def main():
    inventory = {}
    inventory["apple"] = 2
    inventory["rope"] = 10
    inventory["magic boots"] = 2 
    player = Player(get_name())
    print(player.name)
    display_inventory(inventory, 3, 3)
def get_name():
    return input("Enter your name: ")

def play_game(name):
    ...


if __name__ == "__main__":
    main()
