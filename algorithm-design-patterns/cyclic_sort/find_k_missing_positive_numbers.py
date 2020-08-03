"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
 
Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""

import pytest
from typing import List


# Time complexity is O(n + k) as the last two loops will run O(n) and O(k) respectively
# Space complexity is O(k) for extra numbers
def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    extra_numbers = set()
    for i in range(len(nums)):
        if len(missingNumbers) < k:
            if i + 1 != nums[i]:
                missingNumbers.append(i + 1)
                extra_numbers.add(nums[i])
    i = 1

    # We need to have k numbers in the missing numbers array which means
    # that in this case the sorted array will be [5, -1, 3, 4, 5] and [1, 2] will be
    # the missing numbers array. We need to find the next smallest positive number which
    # will come from outside the array.
    while len(missingNumbers) < k:
        candidate_number = i + n
        if candidate_number not in extra_numbers:
            missingNumbers.append(candidate_number)
        i += 1
    return missingNumbers


find_first_k_missing_positive([3, -1, 4, 5, 5], 3)

test_data = [
    ([3, -1, 4, 5, 5], 3, [1, 2, 6]),
    ([2, 3, 4], 3, [1, 5, 6]),
    ([-2, -3, 4], 2, [1, 2]),
]


@pytest.mark.parametrize("arr, k, expected", test_data)
def test_find_first_k_missing_positive(
    arr: List[int], k: int, expected: List[int],
):
    # for item in expected:
    assert find_first_k_missing_positive(arr, k) == expected
