"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""
import pytest
from typing import List

# Sorting the array will take O(nlogn) time. The search pair will take O(n), and overall
# our algorithm will take O(n^2) time.
# The space complexity will be O(n) ignoring the space required for the output array.
def search_triplets(array: List[int]) -> List[int]:
    arr = array[:]
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        current_sum = arr[i]
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    # [-3, -2, -1, 0, 1, 1, 2]
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip the same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip the same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with bigger sum
        else:
            right -= 1  # we need a pair with smaller sum


test_data = [
    ([-3, 0, 1, 2, -1, 1, -2], [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]),
    ([-5, 2, -1, -2, 3], [[-5, 2, 3], [-2, -1, 3]]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_search_triplets(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert search_triplets(arr) == expected
