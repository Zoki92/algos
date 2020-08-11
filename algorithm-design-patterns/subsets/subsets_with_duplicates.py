"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.
"""
import pytest
from typing import List


"""
Since, in each step, the number of subsets could double (if not duplicate) as we add each element to all the existing subsets,
the time complexity of the above algorithm is O(2^N), where ‘N’ is the total number of elements in the input set.
This also means that, in the end, we will have a total of O(2^N) subsets at the most.
Space complexity #
All the additional space used by our algorithm is for the output list. Since at most we will have a total of O(2^N) subsets,
the space complexity of our algorithm is also O(2^N).
"""


def find_subsets(nums: List[int]) -> List[int]:
    subsets = []
    nums.sort()
    subsets.append([])
    start_index, end_index = 0, 0

    for i in range(len(nums)):
        start_index = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            set = list(subsets[j])
            set.append(nums[i])
            subsets.append(set)
    return subsets


test_data = [
    ([1, 3, 3], [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]),
    (
        [1, 5, 3, 3],
        [
            [],
            [1],
            [3],
            [1, 3],
            [3, 3],
            [1, 3, 3],
            [5],
            [1, 5],
            [3, 5],
            [1, 3, 5],
            [3, 3, 5],
            [1, 3, 3, 5],
        ],
    ),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_subsets(arr, expected):
    assert find_subsets(arr) == expected
