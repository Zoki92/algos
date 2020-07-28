"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""
import pytest
from typing import List
import math


def shortest_window_sort(arr: List[int]) -> int:
    low, high = 0, len(arr) - 1

    # find the first number out of sorting order from the begining
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    if low == len(arr) - 1:
        return 0

    while high > 0 and arr[high] > arr[high - 1]:
        high -= 1

    print(f"high: {high} low: {low}")

    # find max and min of the subarray
    subarray_max = -math.inf
    subarray_min = math.inf
    for k in range(low, high + 1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    # extends the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1

    # extend the subarray to include any number which is smaller than the maximum of the subarray

    while high < len(arr) - 1 and arr[high + 1] < subarray_max:
        high += 1

    print(f"min: {subarray_min} max: {subarray_max}")
    print(f"high: {high} low: {low}")
    return high - low + 1


test_data = [
    ([1, 2, 5, 3, 7, 10, 9, 12], 5),
    ([1, 3, 2, 0, -1, 7, 10], 5),
    ([1, 2, 3], 0),
    ([3, 2, 1], 3),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_shortest_window_sort(arr: List[int], expected: int):
    # for item in expected:
    assert shortest_window_sort(arr) == expected


# [1, 2, 5, 3, 7, 10, 9, 12]
# first low = 5, low = 2
# first high = 10, high = 5
# max and min of the subarray
# max = 10
# min = 3
# this will include 9, so low stays the same = 2, while high goes up once 5+1=6
# so our array will be from 6 - 2 + 1 = 5

# [1, 3, 2, 0, -1, 7, 10]
# first low will be 2, position 1,
# first high will be at 0, position 4,
# min = -1 , max = 3
# high = 4, low = 0, high - low + 1

