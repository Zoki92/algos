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
from collections import deque

# The time complexity of the above algorithm is O(logN + K*logK).
# We need O(logN) for Binary Search and O(K*logK) to insert
# the numbers in the Min Heap, as well as to sort the output array.
def find_closest_elements(arr: List[int], K: int, X: int) -> List[int]:
    index = binary_search(arr, X)
    low, high = index - K, index + K
    low = max(low, 0)  # should not be less than 0
    high = min(high, len(arr) - 1)  # should not be higher than the size of the array
    min_heap = []
    # add all candidate elements to the min heap, sorted by their absolute difference from X
    for i in range(low, high + 1):
        heappush(min_heap, (abs(arr[i] - X), arr[i]))
    result = []
    # we need the top K elements having smallest difference from X
    for _ in range(K):
        result.append(heappop(min_heap)[1])
    return result


# two pointers version
# The time complexity of the above algorithm is O(logN + K).
# We need O(logN) for Binary Search and O(K)O(K)O(K) for finding the ‘K’ closest numbers using the two pointers.
# If we ignoring the space required for the output list, the algorithm runs in constant space O(1).
def find_closest_elements_tpv(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    left_pointer, right_pointer = index, index + 1

    n = len(arr)
    for i in range(K):
        if left_pointer >= 0 and right_pointer < n:
            print("left pointer: ", left_pointer)
            diff1 = abs(X - arr[left_pointer])
            diff2 = abs(X - arr[right_pointer])
            if diff1 <= diff2:
                result.appendleft(arr[left_pointer])
                left_pointer -= 1
            else:
                result.append(arr[right_pointer])
                right_pointer += 1
        elif left_pointer >= 0:
            result.appendleft(arr[left_pointer])
            left_pointer -= 1
        elif left_pointer < n:
            result.append(arr[right_pointer])
            right_pointer += 1
    return list(result)


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


@pytest.mark.parametrize("arr, k, x, expected", test_data)
def test_find_closest_elements_tpv(arr, k, x, expected):
    assert find_closest_elements_tpv(arr, k, x).sort() == expected.sort()
