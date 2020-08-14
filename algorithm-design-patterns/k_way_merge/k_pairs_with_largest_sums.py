"""
Given two sorted arrays in descending order, find ‘K’ pairs with the largest
sum where each pair consists of numbers from both the arrays.

Example 1:

Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

Example 2:

Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2]
"""
import pytest
from heapq import *

# Since, at most, we’ll be going through all the elements of both arrays and we will add/remove one element in
# the heap in each step, the time complexity of the above algorithm will be O(N*M*logK) where ‘N’ and ‘M’ are the
# total number of elements in both arrays, respectively.
# If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to O(K^2logK),
# because we are not iterating more than ‘K’ elements in both arrays.
# The space complexity will be O(K) because, at any time, our Min Heap will be storing ‘K’ largest pairs.
def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                # if the sum of the two numbers from the two arrays is smaller than the smallest
                # element of the heap we can break here. Since the arrays are sorted in the descending
                # order we will not be able to find a pair with higher sum moving forward
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    # we have a pair with larger sum remove top and insert this pair in the heap
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))
    result = []
    for (num, i, j) in min_heap:
        result.append([nums1[i], nums2[j]])
    return result


test_data = [
    ([9, 8, 2], [6, 3, 1], 3, [[9, 3], [9, 6], [8, 6]]),
    ([5, 2, 1], [2, -1], 3, [[5, 2], [5, -1], [2, 2]]),
]


@pytest.mark.parametrize("nums1, nums2, k, expected", test_data)
def test_find_k_largest_pairs(nums1, nums2, k, expected):
    assert find_k_largest_pairs(nums1, nums2, k).sort() == expected.sort()
