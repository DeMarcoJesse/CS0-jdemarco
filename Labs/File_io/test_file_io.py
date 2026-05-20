"""Modue to test file_io.py
"""

import file_io


def test_sort_ascending1():
    my_nums = [10, 9, 0, -6]
    file_io.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-6, 0, 9, 10])

# add 3 more test cases in separate test functions
def test_sort_ascending2():
    my_nums = [9, 23, 4, -20]
    file_io.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-20, 4, 9, 23])

def test_sort_ascending3():
    my_nums = [3, 1, 2]
    file_io.sortListInAscendingOrder(my_nums)
    assert (my_nums == [1, 2, 3])


def test_sort_ascending4():
    my_nums = [5, -1, 4, 0]
    file_io.sortListInAscendingOrder(my_nums)
    assert (my_nums == [-1, 0, 4, 5])









def test_sort_descending1():
    my_nums = [0, -10, -1, 5, 100]
    file_io.sortListInDescendingOrder(my_nums)
    my_nums == [100, 5, 0, -1, -10]


# add 3 more test cases in seeparate test functions
def test_sort_descending2():
    my_nums = [0, -10, -1, 5, 100]
    file_io.sortListInDescendingOrder(my_nums)
    assert (my_nums == [100, 5, 0, -1, -10])

def test_sort_descending3():
    my_nums = [3, 1, 2]
    file_io.sortListInDescendingOrder(my_nums)
    assert (my_nums == [3, 2, 1])


def test_sort_descending4():
    my_nums = [7, -2, 0, 5]
    file_io.sortListInDescendingOrder(my_nums)
    assert (my_nums == [7, 5, 0, -2])