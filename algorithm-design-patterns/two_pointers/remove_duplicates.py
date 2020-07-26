"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
after removing the duplicates in-place return the new length of the array.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

"""
import pytest
from typing import List


# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
# The algorithm runs in constant space O(1).
def remove_duplicates(arr: List[int]) -> int:

    next, next_non_duplicate = 1, 1

    while next <= len(arr) - 1:
        if arr[next_non_duplicate - 1] != arr[next]:
            arr[next_non_duplicate] = arr[next]
            next_non_duplicate += 1
        next += 1

    return next_non_duplicate


test_data = [
    ([2, 3, 3, 3, 6, 9, 9], 4),
    ([2, 2, 2, 11], 2),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_remove_duplicates(
    arr: List[int], expected: int,
):
    # for item in expected:
    assert remove_duplicates(arr) == expected

