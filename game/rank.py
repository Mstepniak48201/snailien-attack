class TestItem:
    def __init__(self):
        self.name = "sword"
        self.points = 1

class TestItemNotIncluded:
    def __init__(self):
        self.name = "rocket ship"
        self.points = 1

class Rank:
    def __init__(self):
        self.rank = 0
        self.points = 0
        # Create a dictionary of items and their status.
        self.items = {
            "sword": False,
            "apple": False,
            "pick": False
        }

    """
    def has_item(self, item):
        # Call in the "if item picked up" statement.
        # Check if item exists.
        if item in self.items:
            # Check if item is set to False
            if not self.items[item]:
                print(f"{item } is {self.items[item]}")
                self.items[item] = True
            else:
                print(f"{item} is already True")
    """

    def has_item(self, item):
        item_name = item.name
        if item_name in self.items:
            if not self.items[item_name]:
                print(f"total points: {self.points}")
                print(f"{item_name} is {self.items[item_name]}")
                self.items[item_name] = True
                self.points += item.points
            else:
                print(f"total points: {self.points}")
                print(f"{item_name} is {self.items[item_name]}")
                self.points = self.points
        else:
            print(f"total points: {self.points}")
            print(f"{item_name} is doesn't exist yet.")
            self.items[item_name] = True
            self.points += item.points


rank = Rank()
counter = 0

while counter < 10:
    test_item = TestItem()
    test_item_2 = TestItem()
    test_item_n_i = TestItemNotIncluded()
    rank.has_item(test_item)
    rank.has_item(test_item_2)
    rank.has_item(test_item_n_i)
    counter += 1
    



