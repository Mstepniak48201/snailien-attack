import pytest

from level_1 import get_item_chance

def test_get_item_chance_current_steps():
    assert get_item_chance(10, 75) == False

def test_get_item_chance_total_steps():
    assert get_item_chance(11, 76) == False

def test_get_item_chance_random():
    true_count = 0
    false_count = 0

    for _ in range(100):
        result = get_chance(11, 75)
        if result:
            true_count += 1
        else:
            false_count += 1

    assert true_count > 0
    assert false_count > 0


