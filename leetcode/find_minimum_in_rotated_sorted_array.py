"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0


"""
import pytest
from typing import List


# Time complexity is O(logN) where N is the number of items in the array
# Space complexity is O(1)
def find_min(nums: List[int]) -> int:
    # if there's only one element in the arr we return it
    if len(nums) == 1:
        return nums[0]
    start, end = 0, len(nums) - 1

    # if last element is bigger than the first one then there's no rotation
    if nums[start] < nums[end]:
        return nums[start]
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[start]:
            start = mid + 1
        else:
            end = mid - 1


test_data = [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_find_mid(nums, expected):
    assert find_min(nums) == expected
