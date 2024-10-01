import math
import utils
import time

def main():
    inventory = {
        "sword": 1,
        "apple": 5,
        "magic boots": 1,
        "healing potion": 3,
        "rope": 10
    }

    inventory_display = display_inventory(inventory, 3, 3)

    time.sleep(2)

    close_inventory(inventory_display)

# Functions that take inventory as a parameter:
# [x] get_max_key()
# [x] get_item_list()
# [x] get_quantity_list()

# suppose that instead of an inventory dict, an array of dictionarys is passed:
# [{"sword": 1}, {"sword: 1"}, {"apple": 2}]




def display_inventory(inventory, rows, columns):
    utils.insert_newline()
    max_key = get_max_key(inventory)
    cell_width = len(max_key) + 4
    item_list = get_item_list(inventory, rows, columns)
    quantity_list = get_quantity_list(inventory, rows, columns)
    item_rows = get_content_rows(item_list, rows)
    quantity_rows = get_content_rows(quantity_list, rows)
    grid(item_rows, quantity_rows, cell_width)
    return {"rows": rows, "columns": columns}
    
def grid(item_rows, quantity_rows, cell_width):
    cell_top = f" {cell_width * '_'} "
    cell_margin = f"|{cell_width * ' '}|"
    cell_bottom = f"|{cell_width * '_'}|"
    for i in range(len(item_rows)):
        item_sublist = item_rows[i]
        quantity_sublist = quantity_rows[i]
        columns = len(item_sublist)
        cell_borders(cell_top, cell_width, columns)
        cell_borders(cell_margin, cell_width, columns)
        cell_content(item_sublist, cell_width, columns)
        cell_content(quantity_sublist, cell_width, columns)
        cell_borders(cell_bottom, cell_width, columns)

def inventory_decision():
    user_input = input(f"To discard an item, press D. Press I to close inventory. ").lower()
    return user_input

def close_inventory(row_column_dict):
    row_height = int(row_column_dict["rows"]) * 5 + 3
    utils.erase_lines(row_height)

def get_max_key(inventory):
    if len(inventory) == 0:
        return "░░░"
    key_list = []
    for item in inventory:
        key = list(item.keys())[0]
        key_list.append(key)
    max_len = -1
    for key in key_list:
        if len(key) > max_len:
            max_len = len(key)
            max_key = key
    return max_key

"""
def get_max_key(inventory):
    if len(inventory) == 0:
        return "░░░"
    key_list = []
    for key in inventory:
        key_list.append(key)
    max_len = -1
    for key in key_list:
        if len(key) > max_len:
            max_len = len(key)
            max_key = key
    return max_key
"""

def get_item_list(inventory, rows, columns):
    key_list = []
    required_length = int(rows) * int(columns)
    for item in inventory:
        key = list(item.keys())[0]
        key_list.append(key)
    if len(key_list) < required_length:
        while len(key_list) < required_length:
            key_list.append(" ")
    return key_list

"""
def get_item_list(inventory, rows, columns):
    key_list = []
    required_length = int(rows) * int(columns)
    for key in inventory:
        key_list.append(key)
    if len(key_list) < required_length:
        while len(key_list) < required_length:
            key_list.append(" ")
    return key_list
"""


def get_quantity_list(inventory, rows, columns):
    value_list = []
    required_length = int(rows) * int(columns)
    for item in inventory:
        value = list(item.values())[0]
        value_list.append(value)
    if len(value_list) < required_length:
        while len(value_list) < required_length:
            value_list.append(0)
    return value_list

"""
def get_quantity_list(inventory, rows, columns):
    value_list = []
    required_length = int(rows) * int(columns)
    for value in inventory.values():
        value_list.append(value)
    if len(value_list) < required_length:
        while len(value_list) < required_length:
            value_list.append(0)
    return value_list
"""

def get_content_rows(item_list, rows):
    rows_list = []
    step = int(len(item_list) / int(rows))
    for i in range(0, len(item_list), step):
        rows_list.append(item_list[i:i + step])
    return rows_list

def cell_borders(border, cell_width, columns):
    for i in range(int(columns)):
        if i == int(columns) - 1:
            print(border)
        else:
            print(border, end=" ")

def cell_content(sublist, cell_width, columns):
    item_list = []
    for i in range(int(columns)):
        current_item = sublist[i]
        if current_item == 0:
            current_item = " "
        else:
            item_list.append(current_item)
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
    return item_list 



# Export function
def get_capacity(inventory, rows, columns):
    total_capacity = int(rows) * int(columns)
    full_slots = len(inventory.items())
    empty_slots = total_capacity - full_slots
    return empty_slots


if __name__ == "__main__":
    main()
