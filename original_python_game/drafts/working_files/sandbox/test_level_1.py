import pytest
from level_1 import get_item_chance, level_1_terrain, render_castle

def test_get_item_chance_current_steps():
    assert get_item_chance(10, 71) == False

def test_get_item_chance_total_steps():
    assert get_item_chance(11, 73) == False

def test_get_item_chance_random():
    true_count = 0
    false_count = 0

    for _ in range(100):
        result = get_item_chance(11,71)
        if result:
            true_count += 1
        else:
            false_count += 1

    assert true_count > 0
    assert false_count > 0

def test_level_1_terrain():
    assert level_1_terrain("x", 10) == "xxxxxxxxxx"

def test_render_castle(capfd):
    brick = "x"
    stone = "#"

    render_castle(brick, stone)

    out, err = capfd.readouterr()

    expected_output = (
        f"\x1b[80C{brick}{stone * 3}{brick}\n"
        f"\x1b[80C{stone * 2}   {stone * 2}{brick}\n"
        f"\x1b[80C{stone * 2}   {stone * 2}{brick}\n"
    )

    assert out == expected_output

