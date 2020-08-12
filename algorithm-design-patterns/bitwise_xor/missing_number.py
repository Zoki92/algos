"""
Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.

Input: 1, 5, 2, 6, 4
Answer: 3

"""
import pytest
from typing import List

# Time & Space complexity: The time complexity of the above algorithm is O(n) and the space complexity is O(1)
# cons: While finding the sum of numbers from 1 to n, we can get integer overflow when n is large.
def find_missing_number(arr: List[int]):
    n = len(arr) + 1
    s1 = 0
    for i in range(1, n + 1):
        s1 += i

    for i in arr:
        s1 -= i

    return s1


# Time & Space complexity: The time complexity of the above algorithm is O(n) and the space complexity is O(1)
# won't get overflow
def find_missing_number_xor(arr: List[int]) -> int:
    n = len(arr) + 1
    x1 = 1

    for i in range(2, n + 1):
        x1 = x1 ^ i

    x2 = arr[0]
    for i in range(1, n - 1):
        x2 = x2 ^ arr[i]

    return x1 ^ x2


@pytest.mark.parametrize("arr, expected", [([1, 5, 2, 6, 4], 3)])
def test_find_missing_number(arr, expected):
    assert find_missing_number(arr) == expected


@pytest.mark.parametrize("arr, expected", [([1, 5, 2, 6, 4], 3)])
def test_find_missing_number_xor(arr, expected):
    assert find_missing_number_xor(arr) == expected
