import json

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
                self.__dict__.update({key: value for key, value in item.items() if key != "name"})
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
