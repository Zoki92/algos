"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
"""
import pytest
from typing import List
from heapq import *


# The time complexity of the above algorithm is O(N+N*logK).
# The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap.
# For the frequency map, however, we need to store all the ‘N’ numbers.
def find_k_frequent_numbers(nums: List[int], k: int) -> List[int]:
    num_frequency = {}
    for num in nums:
        num_frequency[num] = num_frequency.get(num, 0) + 1
    min_heap = []
    for num, frequency in num_frequency.items():
        heappush(min_heap, (frequency, num))
        if len(min_heap) > k:
            heappop(min_heap)
    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[1])
    return top_numbers


find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)

test_data = [
    ([1, 3, 5, 12, 11, 12, 11], 2, [[11, 12]]),
    ([5, 12, 11, 3, 11], 2, [[11, 5], [12, 11], [11, 3]]),
]


@pytest.mark.parametrize("nums, k, expected", test_data)
def test_find_k_frequent_numbers(nums, k, expected):
    assert find_k_frequent_numbers(nums, k) in expected
