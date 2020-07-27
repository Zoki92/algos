"""
Given an array with positive numbers and a target number, find all of its contiguous 
subarrays whose product is less than the target number.

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""
import pytest
from collections import deque
from typing import List


# Therefore overall, our algorithm will take O(N^3). Space O(N) without the result
# with result So, at the most, we need a space of O(n^2) for all the output lists.
def find_subarrays(arr: List[int], target: int) -> List[int]:
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with subarray containing only arr[right] and then extend it
        temp_list = deque()

        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


test_data = [
    ([2, 5, 3, 10], 30, [[2], [5], [2, 5], [3], [5, 3], [10]]),
    ([8, 2, 6, 5], 50, [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]),
]


@pytest.mark.parametrize("arr, target, expected", test_data)
def test_find_subarrays(
    arr: List[int], target: int, expected: List[int],
):
    # for item in expected:
    assert find_subarrays(arr, target) == expected


find_subarrays([2, 5, 3, 10], 30)
