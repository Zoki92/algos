"""We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.

Input: [1, 4, 4, 3, 2]
Output: 4

Input: [2, 1, 3, 3, 5, 4]
Output: 3

Input: [2, 4, 1, 4, 4]
Output: 4
"""
import pytest
from typing import List

# time complexity is O(n)
# space complexity is O(1) but modifies the array
def find_duplicate(nums: List[int]) -> int:
    i, n = 0, len(nums)
    # [2, 1, 3, 3, 5, 4]
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1


def find_duplicate_no_modify(nums: List[int]) -> int:
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # find cycle length
    current = nums[nums[slow]]
    cycle_length = 1
    while current != nums[slow]:
        current = nums[current]
        cycle_length += 1

    pointer1, pointer2 = nums[0], nums[0]
    # move pointer2 ahead cycle length steps
    while cycle_length > 0:
        pointer2 = nums[pointer2]
        cycle_length -= 1

    # increment both pointers until they meed at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = nums[pointer1]
        pointer2 = nums[pointer2]

    return pointer1


test_data = [
    ([1, 4, 4, 3, 2], 4),
    ([2, 1, 3, 3, 5, 4], 3),
    ([2, 4, 1, 4, 4], 4),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_duplicate(
    arr: List[int], expected: int,
):
    # for item in expected:
    assert find_duplicate(arr) == expected


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_duplicate_no_modify(
    arr: List[int], expected: int,
):
    # for item in expected:
    assert find_duplicate_no_modify(arr) == expected
