"""Unit test module for cups
"""

from cups import sort_cups


def test_sort_cups_1() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {100: 'red', 10: 'blue', 50: 'yellow'}
    sorted_cups = sort_cups(cups)
    expected = ['blue', 'yellow', 'red']
    assert sorted_cups == expected


# FIXME6 : add a unit test function
def test_sort_cups_2() -> None:
    """test if the cups are sorted correctly."""
    cups = {'green': 30, 'purple': 10, 'orange': 20}
    sorted_cups = sort_cups(cups)
    expected = ['purple', 'orange', 'green']
    assert sorted_cups == expected

# FIXME7 : add a unit test function
def test_sort_cups_3() -> None:
    """test if one cup works correctly."""
    cups = {'black': 15}
    sorted_cups = sort_cups(cups)
    expected = ['black']
    assert sorted_cups == expected


# FIXME8 : add a unit test function
def test_sort_cups_4() -> None:
    """test if cups are already sorted."""
    cups = {'tall': 1, 'grande': 2, 'venti': 3}
    sorted_cups = sort_cups(cups)
    expected = ['tall', 'grande', 'venti']
    assert sorted_cups == expected

# FIXME9 : add a unit test function
def test_sort_cups_5() -> None:
    """test another cup order."""
    cups = {'silver': 40, 'gold': 5, 'bronze': 25}
    sorted_cups = sort_cups(cups)
    expected = ['gold', 'bronze', 'silver']
    assert sorted_cups == expected

# FIXME10 : add a unit test function
def test_sort_cups_6() -> None:
    """test two cups."""
    cups = {'red': 8, 'blue': 2}
    sorted_cups = sort_cups(cups)
    expected = ['blue', 'red']
    assert sorted_cups == expected