"""
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).

Example 2:

Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
number (8) is 12 (5+7).
"""
import pytest
from typing import List
from heapq import *

# Since we need to put all the numbers in a min-heap, the time complexity of the
# above algorithm will be O(N*logN) where ‘N’ is the total input numbers.
# The space complexity will be O(N), as we need to store all the ‘N’ numbers in the heap.
def find_sum_of_elements(nums, k1, k2):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)

    for _ in range(k1):
        heappop(min_heap)

    element_sum = 0
    for _ in range(k2 - k1 - 1):
        element_sum += heappop(min_heap)

    return element_sum


# alternate solution
# We can iterate the array and use a max-heap to keep track of the top K2 numbers.
# We can, then, add the top K2-K1-1 numbers in the max-heap to find the sum of all
# numbers coming between the K1’th and K2’th smallest numbers.
def find_sum_of_elements_alternate(nums, k1, k2):
    max_heap = []
    for i in range(len(nums)):
        # keep smallest k2 numbers in max heap
        if i < k2 - 1:
            heappush(max_heap, -nums[i])
        elif nums[i] < -max_heap[0]:
            heappop(max_heap)  # as we are only interested in the smallest k2 numbers
            heappush(max_heap, -nums[i])

    elements_sum = 0
    for _ in range(k2 - k1 - 1):
        elements_sum += -heappop(max_heap)
    return elements_sum


test_data = [
    ([1, 3, 12, 5, 15, 11], 3, 6, 23),
    ([3, 5, 8, 7], 1, 4, 12),
]


@pytest.mark.parametrize("nums, k1, k2, expected", test_data)
def test_find_sum_of_elements(nums, k1, k2, expected):
    assert find_sum_of_elements(nums, k1, k2) == expected


@pytest.mark.parametrize("nums, k1, k2, expected", test_data)
def test_find_sum_of_elements_alternate(nums, k1, k2, expected):
    assert find_sum_of_elements_alternate(nums, k1, k2) == expected
