import math

inventory = {
    "sword": 1,
    "apple": 5,
    "magic boots": 1,
    "healing potion": 3,
    "rope": 10
}

# Steps
# Get longest key (to determine cell width)
# [x] Inventory is passed to function
# [x] Create list of keys
# [x] Find longest item in key list, and set its value and length to respective variables.
# [x] Abstract into a function, returning a dictionary {max_key: max_len}

# Get item list, and add blank entries based on rows * columns input
# [x] Pass in rows and columns as parameters for display_inventory(), and pass in 2, 3 into the test function.
# [x] Create function that returns a full item list, lengthening the list to (rows * columns) if need be.

# Each cell is comprised of five rows: Top, Margin, Item, Quantity, and Bottom
# Each row must be printed individually by column, like so:
# Suppose 3 columns: Top Top Top \n Margin Margin Margin \n Item Item Item, etc.

# [x] Write a function that prints out the Top cell row dynamically based on the columns and the cell_width parameters.

# The Item list must be split based on the Total Items / Rows (wherein "Rows" with a capital "R" is the grid parameter passed to the function).
# [x] Write a test function to split the Item list.

# Chicken and the egg problem:
# Now Items are split into a list of sublists, where the Sublists are equal in number to the number of rows in the grid, and the number of Items in the Sublists are equal in number to the number of columns in the grid.
# For sublist in list:
# For item in sublist:
# print cell top
# print cell margin
# print cell item
# print cell quantity
# print cell bottom
# [ ] Write a function that prints out n columns of cells.
# [ ] Write a function that prints out the cells themselves, based on the breakdown of the Item list being split.

def display_inventory(inventory, rows, columns):
    max_key = get_max_key(inventory)
    cell_width = len(max_key) + 4
    item_list = get_item_list(inventory, rows, columns)
    item_rows = get_content_rows(item_list, rows)
    quantity_list = get_quantity_list(inventory, rows, columns)
    quantity_rows = get_content_rows(quantity_list, rows)
    grid(item_rows, quantity_rows, cell_width)

    
def get_max_key(inventory):
    key_list = []
    for key in inventory:
        key_list.append(key)
    
    # Initialize the max_len variable that will be
    # compared to all values in the list
    # Set max_key and max_len to the longest key and its length, respectively.
    max_len = -1
    for key in key_list:
        if len(key) > max_len:
            max_len = len(key)
            max_key = key
    return max_key

def get_item_list(inventory, rows, columns):
    key_list = []
    required_length = int(rows) * int(columns)
    for key in inventory:
        key_list.append(key)
    if len(key_list) < required_length:
        while len(key_list) < required_length:
            key_list.append(" ")
    return key_list

def get_quantity_list(inventory, rows, columns):
    value_list = []
    required_length = int(rows) * int(columns)
    for value in inventory.values():
        value_list.append(value)
    if len(value_list) < required_length:
        while len(value_list) < required_length:
            value_list.append(0)
    return value_list

def get_content_rows(item_list, rows):
    rows_list = []
    step = int(len(item_list) / int(rows))
    for i in range(0, len(item_list), step):
        rows_list.append(item_list[i:i + step])
    return rows_list

"""
def cell_top(cell_width, columns):
    cell_top = f" {cell_width * '_'} "
    for i in range(int(columns)):
        if i == int(columns) - 1:
            print(cell_top)
        else:
            print(cell_top, end=" ")

def cell_margin(cell_width, columns):
    cell_margin = f"|{cell_width * ' '}|"
    for i in range(int(columns)):
        if i == int(columns) - 1:
            print(cell_margin)
        else:
            print(cell_margin, end=" ")
"""

def cell_content(sublist, cell_width, columns):
    # Get current item
    for i in range(int(columns)):
        current_item = sublist[i]
        if current_item == 0:
            current_item = " "
        current_item_len = len(str(current_item))
        space_around = int(cell_width - current_item_len)
        if space_around % 2 == 0:
            margin = int(space_around / 2)
            cell_item = f"|{margin * ' '}{current_item}{margin * ' '}|"
            if i == int(columns) - 1:
                print(cell_item)
            else:
                print(cell_item, end=" ")
        else:
            margin_left = int(math.floor(space_around / 2))
            margin_right = int(margin_left + 1)
            cell_item = f"|{margin_left * ' '}{current_item}{margin_right * ' '}|"
            if i == int(columns) - 1:
                print(cell_item)
            else:
                print(cell_item, end=" ")
"""
def cell_bottom(cell_width, columns):
    cell_bottom = f"|{cell_width * '_'}|"
    for i in range(int(columns)):
        if i == int(columns) - 1:
            print(cell_bottom)
        else:
            print(cell_bottom, end=" ")
"""

def cell_borders(border, cell_width, columns):
    for i in range(int(columns)):
        if i == int(columns) - 1:
            print(border)
        else:
            print(border, end=" ")

# len(sublist) is equal to columns, so pass that to the cell creation functions.
def grid(item_rows, quantity_rows, cell_width):
    cell_top = f" {cell_width * '_'} "
    cell_margin = f"|{cell_width * ' '}|"
    cell_bottom = f"|{cell_width * '_'}|"
    for i in range(len(item_rows)):
        item_sublist = item_rows[i]
        quantity_sublist = quantity_rows[i]
        columns = len(item_sublist)
        # cell_top(cell_width, columns)
        # cell_margin(cell_width, columns)
        cell_borders(cell_top, cell_width, columns)
        cell_borders(cell_margin, cell_width, columns)
        cell_content(item_sublist, cell_width, columns)
        cell_content(quantity_sublist, cell_width, columns)
        # cell_bottom(cell_width, columns)
        cell_borders(cell_bottom, cell_width, columns)


    

# print(display_inventory(inventory, 2, 3))

display_inventory(inventory, 3, 3)

"""
def construct_grid(inventory):
    item_list = []
    for item in inventory:
        item_list.append(item)
    
    max_len = -1
    for item in item_list:
        if len(item) > max_len:
            max_len = len(item)
            max_item = item

    cell_width = len(max_item) + 4

    if len(item_list) < 6:
        while len(item_list) < 6:
            item_list.append("x")

    # Cell example, cell_width == 18
    cell_top = f" {cell_width * '_'} "
    cell_margin_top = f"|{cell_width * ' '}|"
    # cell_item = f"|  {max_item}  |"

    # Get item margin left
    item_space_around = "to be filled in tomorrow"


    # Get cell midpoint
    cell_midpoint = round(cell_width / 2) + 1

    # Get position for item quantity
    quantity_margin_left = cell_width - cell_midpoint
    quantity_margin_right = cell_width - (len(str(inventory["healing potion"])) + quantity_margin_left)

    # Assemble quantity row
    cell_quantity = f"|{quantity_margin_left * ' '}{inventory['healing potion']}{quantity_margin_right * ' '}|"

    # Cell bottom
    cell_bottom = f"|{cell_width * '_'}|"

    print(cell_top)
    print(cell_margin_top)
    print(cell_item)
    print(cell_quantity)
    print(cell_bottom)
    
    # for best results, configure your terminal to a mono-spaced font, such as Ubuntu Mono Regular,
    # which is what this program was written in.

    #  __________________
    # |                  |
    # |  healing potion  |
    # |        4         |
    # |__________________|

construct_grid(inventory)   
"""

"""
item_list = []
value_list = []

for item in inventory:
    item_list.append(item)
    value_list.append(inventory[item])
"""
