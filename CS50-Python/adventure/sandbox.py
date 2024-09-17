class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10

    def pick_up_item(self, obtainable_items, inventory):
        item = obtainable_items[0]
        if not item in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1

    def view_inventory(self, inventory):
        ...

    def remove_item(self, item, inventory):
        ...

        
        
obtainable_items = ["sword", "magic boots", "apple", "healing potion"]
inventory = {}
player = Player(input("What's your name? "))
print(player.name)

def main():
    player.pick_up_item(obtainable_items, inventory)
    print(inventory)
    player.pick_up_item(obtainable_items, inventory)
    print(inventory)



    

if __name__ == "__main__":
    main()
