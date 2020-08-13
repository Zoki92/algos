"""
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. 
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]

Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]

Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]

"""
import pytest
from typing import List
from heapq import *


def find_closest_elements(arr: List[int], K: int, X: int) -> List[int]:
    index = binary_search(arr, X)
    low, high = index - K, index + K
    low = max(low, 0)
    high = min(high, len(arr) - 1)
    min_heap = []
    for i in range(low, high + 1):
        heappush(min_heap, (abs(arr[i] - X), arr[i]))
    result = []
    for _ in range(K):
        result.append(heappop(min_heap)[1])
    return result


def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if start > 0:
        return start - 1
    return start


find_closest_elements([5, 6, 7, 8, 9], 3, 7)

test_data = [
    ([5, 6, 7, 8, 9], 3, 7, [6, 7, 8]),
    ([2, 4, 5, 6, 9], 3, 6, [4, 5, 6]),
    ([2, 4, 5, 6, 9], 3, 10, [5, 6, 9]),
]


@pytest.mark.parametrize("arr, k, x, expected", test_data)
def test_find_closest_elements(arr, k, x, expected):
    assert find_closest_elements(arr, k, x).sort() == expected.sort()
