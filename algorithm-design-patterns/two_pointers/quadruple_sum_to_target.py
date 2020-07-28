"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

"""
import pytest
from typing import List


# Sorting the array will take O(N∗logN)O. Overall searchQuadruplets() will take O(N * logN + N^3), which is asymptotically
# equivalent to O(N^3).
# The space complexity of the above algorithm will be O(N) which is required for sorting.
def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:
    quadruplets = []
    arr.sort()
    # [-2, -1, 0, 1, 2, 2]

    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)
    return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1
    while left < right:
        sum = arr[first] + arr[second] + arr[left] + arr[right]
        if sum == target_sum:
            quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif target_sum > sum:
            left += 1
        else:
            right -= 1


test_data = [
    ([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
    ([2, 0, -1, 1, -2, 2], 2, [[-2, 0, 2, 2], [-1, 0, 1, 2]]),
]


@pytest.mark.parametrize("arr, target, expected", test_data)
def test_search_quadruplets(
    arr: List[int], target: int, expected: List[List[int]],
):
    # for item in expected:
    assert search_quadruplets(arr, target) == expected
