"""Problem Statement #

Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""
import pytest
from typing import List
from heapq import *

# Since we’ll be going through at most ‘K’ elements among all the arrays, and we will remove/add
# one element in the heap in each step, the time complexity of the above algorithm will be O(K*logM)
# where ‘M’ is the total number of input arrays.
# The space complexity will be O(M) because, at any time, our min-heap will be storing one
# number from all the ‘M’ input arrays.
def find_Kth_smallest(lists, k):
    min_heap = []
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))
    # take the smallest element from the min heap if the running count is equal to k return the number
    number_count, number = 0, 0
    while min_heap:
        number, i, list = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(list) > i + 1:
            heappush(min_heap, (list[i + 1], i + 1, list))

    return number


find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)

test_data = [
    ([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5, 4),
    ([[5, 8, 9], [1, 7]], 3, 7),
]


@pytest.mark.parametrize("lists, k, expected", test_data)
def test_find_Kth_smallest(lists, k, expected):
    assert find_Kth_smallest(lists, k) == expected


"""
Similar Problems #

Problem 1: Given ‘M’ sorted arrays, find the median number among all arrays.

Solution: This problem is similar to our parent problem with K=Median. So if there are ‘N’
total numbers in all the arrays we need to find the K’th minimum number where K=N/2.

Problem 2: Given a list of ‘K’ sorted arrays, merge them into one sorted list.

Solution: This problem is similar to Merge K Sorted Lists except that the input is a list of arrays
compared to LinkedLists. To handle this, we can use a similar approach as discussed in our parent
problem by keeping a track of the array and the element indices.
"""
