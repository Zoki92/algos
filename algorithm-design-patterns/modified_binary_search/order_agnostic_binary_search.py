"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. 
You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Input: [4, 6, 10], key = 10
Output: 2

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4

Input: [10, 6, 4], key = 10
Output: 0

Input: [10, 6, 4], key = 4
Output: 2
"""
import pytest
from typing import List


def binary_search(arr: List[int], key: int) -> int:
    start = 0
    end = len(arr) - 1
    is_ascending = arr[start] < arr[end]
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        if is_ascending:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


test_data = [
    ([4, 6, 10], 10, 2),
    ([1, 2, 3, 4, 5, 6, 7], 5, 4),
    ([10, 6, 4], 4, 2),
]

binary_search([1, 2, 3, 4, 5, 6, 7], 5)


@pytest.mark.parametrize("arr, key, expected", test_data)
def test_binary_search(arr: List[int], key: int, expected: int):
    assert binary_search(arr, key) == expected
