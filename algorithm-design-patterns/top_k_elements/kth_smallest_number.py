"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""
import pytest
from heapq import *

# As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically
# equal to O(N*logK)
# The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
def find_Kth_smallest_number(nums, k):
    max_heap = []
    # put first k numbers in max heap
    for i in range(k):
        heappush(max_heap, -nums[i])

    # go through the remaining numbers in the array, if the number from the array
    # is smaller than the top(biggest) number of the heap, remove the top number from heap
    # and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    return -max_heap[0]


test_data = [
    ([1, 5, 12, 2, 11, 5], 3, 5),
    ([1, 5, 12, 2, 11, 5], 4, 5),
    ([5, 12, 11, -1, 12], 3, 11),
]


@pytest.mark.parametrize("nums, k, expected", test_data)
def test_find_Kth_smallest_number(nums, k, expected):
    assert find_Kth_smallest_number(nums, k) == expected
