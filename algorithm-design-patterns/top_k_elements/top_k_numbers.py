"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""

from heapq import *
import pytest

# As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically
# equal to O(N*logK)
# The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
def find_k_largest_numbers(nums, k):
    min_heap = []
    # put first k numbers in the min heap
    for i in range(k):
        heappush(min_heap, nums[i])
    # go through the remaining numbers of the array, if the number from the array is bigger
    # than the top(smallest) number in the min heap, remove the top number from heap and
    # add the number from the array
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return list(min_heap)


test_data = [
    ([3, 1, 5, 12, 2, 11], 3, [5, 12, 11]),
    ([5, 12, 11, -1, 12], 3, [12, 11, 12]),
]


@pytest.mark.parametrize("nums, k, expected", test_data)
def test_find_k_largest_numbers(nums, k, expected):
    assert find_k_largest_numbers(nums, k).sort() == expected.sort()
