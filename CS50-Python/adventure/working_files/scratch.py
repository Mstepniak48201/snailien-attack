import json
import random

# What I want to do :
# Knowing that an item in a list may have an attribute that has a list as its value, and that the first value on that list may be the string "random:"
# And that the item will be structured like so: ["random", start_int, end_int] and will contain the args for random.randrange():

# I need a function to say:
# for item in list:
# item_key = item[key]
# if type(item_key) == list and item_key[0] == "random":
# self.item_key = my_function(item_key[1], item_key[2])

# def my_function(start, end):
# random.randrange(start, end)


# Small scale test:
"""
test_dic = {
    "name": "foo",
    "list": ["random", 1, 2, 3]
}

test_copy = {}

for key, value in test_dic.items():
    if isinstance(value, list):
        test_copy[key] = "new value"
    else:
        test_copy[key] = value

print(test_copy)
"""

# Convert to Python dictionary.
with open("random_test.json", "r") as file:
    test_data = json.load(file)

class TestClass:
    def __init__(self, name, data=test_data):
        self.name = name
        attributes = {}

        for item in data:
            if item["name"] == self.name:
                for key, value in item.items():
                    if isinstance(value, list) and value[0] == "random":
                        attributes[key] = "some other value"
                    elif key != "name":
                        attributes[key] = value
                break

        for key, value in attributes:
            self.__dict__[key] = value

    def __repr__(self):
        attributes = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"TestClass({attributes})"
        



foo = TestClass("foo")
print(foo)




"""
with open("random_test.json", "r") as file:
    test_data = json.load(file)

class TestClass:
    def __init__(self, name, data=test_data):
        self.name = name

        object_values = {}
        for item in data:
            if item["name"] == self.name:
                for key, value in item.items:



        for item in data:
            for key, value in item.items():
                if isinstance(value, list):
                    item[key] = "new value"


        for item in data:
            if item["name"] == self.name:
                for key, value in item.items():
                    if key != "name":
                        self.__dict__[key] = value
                break

"""
""" 
        dict_items_copy = list(self.__dict__.items())

        for key, value in self.__dict__.items():
            if isinstance(value, list):
                self.__dict__[key] = "new value"
"""

"""
    def __repr__(self):
        attributes = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"TestClass({attributes})"

foo = TestClass("foo")

print(foo)
"""



"""
# Open JSON
with open("test.json", "r") as file:
    # Convert to Python dictionary
    test_data = json.load(file)

class TestClass:
    def __init__(self, name, data=test_data):
        self.name = name
        self.data = data

        for item in data:
            if item["name"] == self.name:
                # The code below works, and I'm keeping it for reference, but I'm refactoring it.
                # self.__dict__.update({key: value for key, value in item.items() if key != "name"})

                # Refactored code for readability:
                for key, value in item.items():
                    if key != "name":
                        # How this works:
                        # When an object of a class is created, Python creates a dictionary-like object named __dict__.
                        # __dict__ stores the object's attributes.
                        # We can access it with self.__dict__
                        # When we write self.__dict__[key] = value, we create an attribute with the name [key], 
                        # and set its value to value.
                        self.__dict__[key] = value
                break

    # Make sure the dict update works.
    def __repr__(self):
        attributes = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"TestClass({attributes})"

    # Make sure everything's working.
    def hello_world(self):
        print(self.data)

test_1 = TestClass("item one")
print(test_1)
"""
