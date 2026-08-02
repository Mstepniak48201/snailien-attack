# SNAILIEN ATTACK!!!

## Video Demo:
Video Url

## Project GitHub: https://github.com/Mstepniak48201/snailien-attack

## How to Start SNAILIEN ATTACK!!!
- SNAILIEN ATTACK!!! has been developed for Linux and Mac. Windows terminal emulators may work, but are not guaranteed.

- The following terminal emulators are supported:
  - Terminator (Linux)
  - Kitty (Mac)
  - Iterm2 (Mac)

- Be advised that Mac's default Terminal application may not render the game correctly.

- Navigate to the project directory.

- The file name to run will depend on which version of SNAILIEN ATTACK!!! you are playing. See description below.

- If you have aliased the Python3 command, you will use that alias, otherwise use the Python3 command as follows.

- Run Game Commands by Version:
  - CS50 Submission Version: Python3 project.py
  - Github development Version: Python3 level\_1.py
  - Future version will be listed here along with game updates.


## Project Description


### Overview
This project started out as a way for me to tackle a problem I was having. I am working on a project in Godot, and I've had a lot of trouble understanding how to build an inventory system. Mind you, I can write code from a tutorial that "works," but often I only understand portion of WHY it works. I decided that for my final project, I would build a terminal game that focused on item collection and a dynamic inventory.

The game I have built is called "SNAILIEN ATTACK!!!" I plan to keep developing this as a terminal game, and at some point, hopefully, you the player, as a snail, get to attack something. But for now, this was about me understanding a bit how to manage state inside of a while loop, so for now, you get to pick up pickaxes, swords, and apples. You can see the player's position, interact with the inventory, and at the end of the level, you (the snail) go into a castle and a flag raises on a pole.

If you're having fun so far, please follow the project at the GitHub link above. I will be building new features as often as I can!

For anyone who is curious, please look through items.json for an idea of what future features will look like! 

This project is structured into nine files, and I will describe them one at a time.


### utils.py
This file is the "backbone" of the game's animation and UI visuals. Using sys.stdout, the time module, and ANSII escape characters, the methods in utils.py do exactly the things they say they do in their names:

  - `insert_newline(n)`

  - `move_element\_forward(spaces, string, sprite, sleep)`

  - `hide_cursor()`

  - `show_cursor()`

  - `move_cursor\_right(n)`

  - `move_cursor\_left(n)`

  - `move_cursor\_up(n)`

  - `move_cursor\_down(n)`

  - `overwrite_line(text)`

  - `erase_line()`

  - `erase_lines(n)`

These utility functions are used to write and overwrite events in the terminal, from animating the snail, to building out the inventory grid. 


### global\_vars.py

This file is where the global variables dealing with the inventory system live: INVENTORY = [], AND INVENTORY\_DICT = {}. It is likely that in the future, this is where HEALTH = 10 will live as well.


### items.json

This was a design choice that was based on the advice of a friend, to whom I was worrying that my Item class was getting pretty cluttered. I've had some back and forth with several friends who have critiqued my approach, but I had a very specific functionality that I wanted to implement, and while I think I can clean it up a bit further, I believe my overall approach is sound. 

In item.py, which will be discussed next, I wanted a game mechanic that would allow me to fulfill several criteria:

  - A counter is set to a random number of steps, n.

  - Every step that is taken, an item has a 1 in 9 chance of spawning.
    - I played with several ratios, and this one had the best game rhythm, in my opinion.

  - The item that spawns will be chosen randomly from a list that is dependent on an internal XP level.

I implemented all but the internal XP ranking, which I have started on and will be a further feature of the game soon. Some of the issues I ran into with this json are that python methods and ANSII escape sequences, which are attributes of some items, are not valid json syntax. In the future, I may refactor this JSON into items.py as a Python Dict, so that I can include these, as they are cluttering up item.py.


### item.py

The first decision I made that item.py would be the only file that has access to the global INVENTORY and `INVENTORY_DICT` variables. Everything else was a journey. I'll start at the point after I decided to use a json, but know that at one point, all the data in items.json was being loaded from within the `__init__`

From the top of the file:

- items.json is imported and read with "with open" and json.load(file)

- class Item is defined, and initialized with self.name = name, self.quantity = 1, and attributes = {}

- I have designed a mechanic for spawning broken items and using a wrench to fix them, and the plan is for the name attribute of those broken items to be "broken item\_name." So the first thing I do after setting the "core" attributes of an item is handle broken items.
  - This mechanic creates a "repaired\_name" attribute to be used in the repair\_item() instance method.

- The next dynamic attribute setter is a match statement that takes in the name attribute passed to Item() when it is instantiated, and sets the self.sprite attribute. These are set here because most of the sprites are bit art that I created from ANSII escape sequences, and they are not valid JSON syntax. 

- The particle effect method within init is a planned on feature for both the "magic boots" item and the potions.

- This next part was the thing that took me a good while to figure out: How to dynamically assign attributes to the instantiated object, based on the "name" parameter passed to it. This functionality is required, since the item name is generated randomly in the @classmethod generate\_item(). I'll break it down with code comments.

- Note: some items have a function that gives them a chance to complete an action. These utilize random.randrange() method. Since functions are not valid JSON syntax, I created a protocol: Such attributes will be set equal to a list, the first item of which will be the str "random." The following values will the the arguments to be passed to the method. For example ["random", 2, 7].

```
# Convert item.json to a Python list of dictionaries.
item_data = json.load(file)

class Item:
  # item_data is passed to __init__ as "data."
  def __init__(self, name, strength=0, data=item_data) 
    self.name = name
    self.quantity = 1
    
    # Create attributes Dict to be mapped dynamically onto self.
    attributes = {}

  ... dynamically handle broken items, ANSII attributes, etc.

  # Iterate through the data list.
  for item in data:
    # Check if the name attribute of an item matches the name passed to __init__.
    if item["name"] == self.name:
      # Get the key and value in a .items() tuple.
      for key, value in item.items():
        # Check if value is a random function.
        if isinstance(value, list) and value[0] == "random":
          # Set the attributes Dict key to the function.
          start = value[1]
          end = value[2]
          attributes[key] = random.randrange(start, end)
        # Handle all other attributes, excluding "name," as that has already been set in __init__
        elif key != value:
          attributes[key] = value

  # Copy attributes Dict entries to self.
  for key, value in attributes.items():
    self.__dict__[key] = value

  # Debugging with __repr__
  def __repr__(self):
    attributes = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
    return f"Item({attributes})"    
```

- Note on the usage of `self.__dict__`: This was something I went back and forth on between getattr() and `self.__dict__`. Stack Exchange articles repeatedly said that getattr() and setattr() could have funny effects on linters, and since I have had trouble with the Code Spaces VS Code linter in the past, I decided to err on the side of caution. I am aware that `self.__dict__` comes with its own set of issues, but as both approaches seemed valid, and the built-in methods seemed more likely to make the linter mad, I decided on `self.__dict__`. Also, as I am new to Python, I wanted to avoid using built-in methods that I really don't understand, and opted for a more bare-bones approach, using a thing that was less of a black box to me, that I was able to dive into with a bit more ease and learn about the mechanics of what's happening under the hood.

- `repair_item()`: instance methad that is called on an instance of the Item() class, and if self.broken = True, sets self.name to the `self.repaired_name` in its attributes.

- `generate_item(cls, rank=0)`: The only rank that exists at the moment is 0, but within each rank there is a list of items. the return value of this class method is the result of random.choice(items)

- `spawn_item(cls, total_steps_taken, item, trail)`: This takes in the item returned from `generate_item()`, and overwrites the entire line, using `total_steps_taken` and "trail" to re-render the snail (player), and place the item in front of the player.

- `no_item_decision`: experimental feature not implemented giving a better message to the player when they attempt to pick up an item twice.

- `item_decision(cls, item, can_pick_up, inventory=INVENTORY)`: takes item, the `can_pick_up` boolean that is set in the main game loop, and the global INVENTORY list as parameters.

There was a lof of tricky utility cursor movement with this function, as it uses input() several times, and every time input is called, a new line results. So there's a fair amount of repositioning of the curosr, erasing lines making way for new prompts, and so on. Also, in this one, I used getattr(), hoping the linter wouldn't yell at me!

Which prompt the player gets depends on whether the item can be equiped, consumed, whether the inventory is full, etc. If the Player has already made the decision to pick up the item, within the main game loop `can_pick_up` will be set to False, and a new prompt without the option to pick the item up will appear.

- `add_item_to_inventory(cls)`: handles stackable items and non-stackable items and appends them to the global INVENTORY list according to their quantities.

- `discard_item(cls)`: handles items that exist for inputs, and non-existent items, and give the appropriate prompts. If an input matching an existing item is given, the item is removed from the global INVENTORY list.

- `update_inventory(cls)`: The inventory UI grid takes a list of dictionaries as a parameter. Each dictionary should have two key value pairs, like so: {name = item.name, quantity = item.quantity}. This function returns that list.


### inventory\_ui.py
`inventory_ui.py` is a functional module in which there is a main fuction, `display_inventory` (inventory, columns, rows) that calls 8 other functions in succession to create the inventory grid.

Features: 
- Grid can be initialized to any size based on rows and columns input.
- Dynamic sizing based on the longest str value in the update\_inventory() list passed in as a parameter.
- Function inventory\_get\_decision() prompts player to discard item or close inventory.
- Function close\_inventory() gets height by row of inventory grid and calls utils.erase\_lines() and sets cursor back to the item\_decision() prompt level (Two cursor levels below the gameplay level)
- Function refresh\_inventory() closes the inventory, but in preparation for the inventory to be immediately written again with updated data (moving up one cursor level fewer than close\_inventory()).
- Function get\_capacity() return the number of empty inventory slots.

- The functions called by display\_inventory() are:
  - Get\_max\_key(): gets the length of the longest key str in the key-value pairs passed in.
  - Get\_item\_list(inventory, rows, columns): returns list of keys.
  - Get\_quantity\_list(inventory, rows, columns): returns list of values.
  - Get\_conten\_rows(): takes in item ("name" attribute) list or quanitity list and returns the content of those rows.
  - Grid(item\_rows, quantity\_rows, cell\_width)

- Description of grid(item\_rows, quantity\_rows, cell\_width):
  - Creates f strings for the cell\_top, cell left and right margin, and cell\_bottom.
  - For each row in len(item\_rows), call the cell\_borders and cell\_content functions to construct the cells.
  - Cells print out based on number of columns, populated with the data from item\_rows and quantity\_rows.


### player.py
The Player class is initialized with self.name, self.sprite, self.counter, and self.slime\_trail.

There are two instance methods within Player():

- handle\_input(self, player\_input, item, can\_pick\_up)
  - Handles input inside the main game loop while the game is paused.
  - If input == "i," sets inventory\_is\_open = True
  - handles all possible choices and error inputs while inventory is open.
  - If input == "e," calls item.add\_item\_to\_inventory()

- handle\_player\_exit(self, total\_steps\_taken, player\_effect, player\_sprite)
This instance method is a bunch of trickery that uses the utility functions and ANSII escape codes to make it appear as if the player is disappearing into the castle at the end of the level, replacing the background color of the "stone" after the player sprite passess it, changing the player sprite's background color to "bright black," the same as the "stone," and making the player sprite disappear behind the castle wall as it enters the doorway.


### ingame\_ui.py
This is a counter that I have used for keeping track of player position as I work through various features. It is unlikely to make it into a further version of the game, but there was one fun thing I learned about:

This ANSII escape code print("\x1b[s", end="") allows me to save the current cursor position.

I can then use my utilities to move the cursor around (and in this case, I move the cursor up, and update the print statement that displays the player's current position.

I can then use print("\x1b[u", end="") to return my cursor to the saved position (in this case, back to the player movement).


### flag.py
This is a simple class that positions the cursor in the necessary places, and renders a flag and flagpole sprites.

The flag is initially rendered in the "down" position, and another instance method will animate the flag running up the pole.


### project.py/level\_1.py
This is the main game file. It consists of four functions:
- level\_1(player): the main game loop
- render\_castle(brick, stone): renders the castle at the end of the level.
- level\_1\_terrain(block, length): renders the terrain under the player.
- get\_item\_chance(current\_steps\_taken, total\_steps\_taken): determines if an item will spawn.

#### level\1(player): Description of main game loop
- numerous sprite variables are initialized.

- steps\_to\_take variable is initialized to random.randrange(10, 26, 3) meaning that whenever the variable is reset at the top of the main game loop (assuming total\_steps\_taken < 83, it will be reinitialized to a number between 10-26, in steps of 3.

- flag.render\_flag\_down() is called.

- render\_castle(brick, stone) is called.

- level\_1\_terrain(block, 45) is called and printed.

- Cursor is moved back up into gameplay position.

- Main gameplay while loop begins:

  ```
  while steps_to_take > 0:
    # Instantiate InGameUI() and call display_position(total_steps_taken)
    # Hide the cursor.

    # Pause Game if at end of level, i.e. if total_steps_taken == 83 game_is_paused = True

    # If steps_to_take == 1: reset to randrange(10, 26, 3)

    # Call get_item_chance() and if it returns true:
      # Generate and spawn item.
      # Set game_is_paused to True.
      # Set can_pick_up to True.
      # Move cursor down 2.

      # while game_is_paused:
        # Set player_input variable equal to the return of Item.item_decision(item, can_pick_up)    
        # Call player.handle_input(), which returns a boolean, and set item_picked_up equal to its return.
        # If item_picked_up:
          # Set can_pick_up = False

        # If player_input == "k":
          # Unpause game and move cursor back to gameplay position.
          # Reset item_picked_up to False and can_pick_up to True.

    # If the game not paused: 
      # Call player.handle_player_exit(): this moves the player, and handles the exit into the castle.
      # Increment total_steps_taken and current_steps_taken by 1, decrement steps_to_take by 1.

    # If total_steps_taken == 83:
      # Call flag.run_up_the_flag()
      # Show cursor.
      # update inventory and call inventory_ui.display_inventory()
  ```

### test\_project.py/test\_level\_1.py

I had run into some problems using the mock library, which is definitely a skill issue, but outside the scope of what I had hoped to gain from this project. I will be learning how to use mocks, but for the purposes of these tests, I avoided it.

Which is why I chose to include `get_item_chance(), level_1_terrain(), and render_castle() in project.py/level_1.py` and test them.

- Testing `get_item_chance()`:

`test_get_item_chance_current_steps()` tests the assertion that if a number that is not > 10 is passed in as the `curent_steps` parameter, the function will return False.

`test_get_item_chance_total_steps()` tests the assertion that if a number that is > 72 is passed in as the `total_steps` parameter, the function will return False.

`test_get_item_chance_random()` tests the randomness of the function by running it 100 times, and keeping track of how many times it returns a Truthy value, and how many times it returns Falsey. The tests assert that there should be at least 1 True value and one False.


- Testing `level_1_terrain()`: `test_level_1_terrain()` tests that the function takes in a str and an int, and returns a str that is equal to {str * int}


- Testing `render_castle`:

`test_render_castle()` is a bit more tricky, as it is testing print statements and ANSII escape keys. As before, I will break it down with comments.
```
  # Pass capfd to the test function as an argument.
  # capfd will allow the function to capture the standard output (and error, if there was one).
  def test_render_castle(capfd):
    # Declare dummy variables.
    brick = "x"
    stone = "#"

    # Call the function 
    render_castle(brick, stone)

    # Use capfd.readouterr() to capture the output. In this case the error will be an empty string.
    # .readouterr() returns a tuple containing two strings: output and error.
    out, err = capfd.readouterr()

    # Group a multiline string that will mock the expected standard output stored in the out variable by .readouterr()
    expected_output = (
      # \x1b[80C is the ANSII escape code to move the cursor 80 spaces, as is done in render_castle()
      f"\x1b[80C{brick}{stone * 3}{brick}\n"
      f"\x1b[80C{stone * 2}   {stone * 2}{brick}\n"
      f"\x1b[80C{stone * 2}   {stone * 2}{brick}\n" 
    )

    # assert that the multiline str stored by .readouterr() in the out variable is equal to the expected_output.
    assert out == expected_output 

```

### GitLab to GitHub Sidequest

I decided about midway through this project that I wanted to make it a public repo on GitHub. The only problem was that it was part of a larger repo on GitLab where I have been keeping all my Python projects. Isolating the project directory, keeping its commit history intact, and migrating the repo to GitHub was quite the adventure. I learned a lot about git through this process, and am looking forward to taking a full course on it in the future.

### Conclusions and next steps

This project started out as a way for me to understand state management within a game loop, and to build an inventory system from scratch, and developed into something that I plan to continue working on. I have been on many "side quests" while building this game, and learned things I had no plans to learn.

My immediate plans for this project are to do some refactoring of item.py, and possibly switch items.json to items.py, in hopes that I can get rid of the match statement dealing with the ANSII escape codes in the `__init__`. The next features I have planned will be a particle effect when an item is picked up, fireworks when a player completes a level, and a more complex level 2 that will introduce obstacles and enemies to the gameplay. Additionally, I will work up a title screen of ASCII art. In the future, I will release the game, for free, on itch.io.

There are things I want to refactor, class methods that should probably be instance methods, and other fixes, but I think it's time to turn this project in!










