"""
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

"""
import pytest
from typing import List


def find_subsets(nums: List[int]) -> List[int]:
    subsets = []
    subsets.append([])
    for current_num in nums:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(current_num)
            subsets.append(set)
    return subsets


"""
1st iteration 
current num = 1
n = 1
for i in range 1 
set = list(subsets[0]) ([])
set.append 1 , subsets = [], [1]

2nd iteration
current num = 3
n = 2
0 1:
    set = []
    set.append 3
    set = [3]
    subsets = [] [1] [3]
0 1:
    set = subsets[1]
    set.append(3) 
    set = [1, 3]
    subsets  = [] [1] [3] [1, 3]
"""


test_data = [
    ([1, 5, 3], [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]),
    ([1, 3], [[], [1], [3], [1, 3]]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_subsets(arr, expected):
    assert find_subsets(arr) == expected
