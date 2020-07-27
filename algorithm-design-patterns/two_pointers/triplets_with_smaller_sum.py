"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it 
such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
Write a function to return the count of such triplets.

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""
import pytest
from typing import List


def triplet_with_smaller_sum(arr: List[int], target: int) -> int:
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        right = len(arr) - 1
        left = i + 1
        # [-1, 1, 2, 3, 4]
        # From the problem we see that any items between left and right should be counted
        # because their sum is less than the target, hence the right - left.
        while left < right:
            if target > arr[i] + arr[left] + arr[right]:  # found the triplet
                # since arr[right] >= arr[left] we replace arr[right] by any number between
                # left and right to get a sum less than the target sum
                count += right - left
                left += 1
            else:
                right -= 1
    return count


test_data = [
    ([-1, 0, 2, 3], 3, 2),
    ([-1, 4, 2, 1, 3], 5, 4),
]


@pytest.mark.parametrize("arr, target, expected", test_data)
def test_triplet_with_smaller_sum(
    arr: List[int], target: int, expected: int,
):
    # for item in expected:
    assert triplet_with_smaller_sum(arr, target) == expected


# time complexity of this one is O(n^3), space is O(n)
# This algorithm returns the triplets instead of the count
def triplet_with_smaller_sum_list(arr: List[int], target: int) -> List[int]:
    triplets = []
    arr.sort()
    for i in range(len(arr) - 2):
        right = len(arr) - 1
        left = i + 1
        # [-1, 1, 2, 3, 4]
        # From the problem we see that any items between left and right should be counted
        # because their sum is less than the target, hence the right - left.
        while left < right:
            if target > arr[i] + arr[left] + arr[right]:  # found the triplet
                # since arr[right] >= arr[left] we replace arr[right] by any number between
                # left and right to get a sum less than the target sum
                for j in range(right, left, -1):
                    triplets.append([arr[i], arr[left], arr[j]])
                left += 1
            else:
                right -= 1
    return triplets


test_data = [
    ([-1, 0, 2, 3], 3, [[-1, 0, 3], [-1, 0, 2]]),
    ([-1, 4, 2, 1, 3], 5, [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]),
]


@pytest.mark.parametrize("arr, target, expected", test_data)
def test_triplet_with_smaller_sum_list(
    arr: List[int], target: int, expected: List[int],
):
    # for item in expected:
    assert triplet_with_smaller_sum_list(arr, target) == expected

