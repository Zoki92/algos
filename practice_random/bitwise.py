from typing import List

import pytest


def find_missing_number(array: List[int]):
    """Given an array of n-1 integers in the range from 1 to n, find the missing number

    So here we need to grab the all the numbers in that range
    so for the example bellow, we have array of 5 items, and we need to grab 1 to n, so that's 5 + 2 since python doesn't take last
    value in the range function, (range(2, 7) max num is 6)
    """
    all_values = 1
    array_length = len(array) + 1
    for i in range(2, array_length + 1):
        print(f"before {all_values}")
        print(f"the i : {i}")
        all_values = all_values ^ i
        print(f"after {all_values}")
    print("===============================")
    array_values = array[0]
    for i in range(1, array_length - 1):
        print(f"before {array_values}")
        print(f"the i {array[i]}")
        array_values = array_values ^ array[i]
        print(f"after {array_values}")

    return all_values ^ array_values


"""
Time complexity is O(n) and space complexity is O(1)
"""

test_data_fmn = [([1, 5, 2, 6, 4], 3)]


@pytest.mark.parametrize("array, expected", test_data_fmn)
def test_find_missing_number(array, expected):
    assert find_missing_number(array) == expected


def find_single_number(array: List[int]) -> int:
    """
    In a non-empty array of integers, every number appears twice except for one. Find that single number

    The idea here is to go through all the numbers in the array and use XOR, the duplicates will eliminate themselves

    Time complexity is O(n) and space complexity is O(1)
    """
    missing = 0
    for i in array:
        missing = missing ^ i
    return missing


test_data_fsn = [
    ([1, 4, 2, 1, 3, 2, 3], 4),
    ([7, 9, 7], 9),
]


@pytest.mark.parametrize("array, expected", test_data_fsn)
def test_find_single_number(array, expected):
    assert find_single_number(array) == expected


def find_single_numbers(array: List[int]) -> List[int]:
    """
    In a non empty array of numbers every number appears exactly twice except for two numbers that appear only once. Find those two numbers


    """
    n1xn2 = 0
    for i in array:
        n1xn2 = n1xn2 ^ i
    print(n1xn2)
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    print(f"right most set {rightmost_set_bit}")
    num1, num2 = 0, 0
    for num in array:
        if (num & rightmost_set_bit) != 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


test_data_fsns = [
    ([1, 4, 2, 1, 3, 5, 6, 2, 3, 5], [4, 6]),
    ([2, 1, 3, 2], [1, 3]),
]


@pytest.mark.parametrize("array, expected", test_data_fsns)
def test_find_single_numbers(array: List[int], expected: List[int]) -> None:
    assert find_single_numbers(array).sort() == expected.sort()
