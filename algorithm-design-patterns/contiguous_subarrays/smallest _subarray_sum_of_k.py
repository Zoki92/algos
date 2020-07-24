"""
Smallest Subarray with a given sum 
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is greater 
than or equal to ‘S’. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
"""
import pytest
from typing import List
import math

# This will take O(M * N)  where n is the number of elements in the array and m is the amount of
# subarray members we go through for each element
def smallest_subarray_with_given_sum(s: int, arr: List) -> int:
    smallest_subarray_members = len(arr)
    for i in range(len(arr)):
        if arr[i] >= s:
            return 1
        current_members = 0
        current_sum = 0
        j = i
        while j <= len(arr) - 1 and current_sum < s:
            current_sum += arr[j]
            current_members += 1
            j += 1
        if current_sum >= s:
            smallest_subarray_members = min(smallest_subarray_members, current_members)

    return smallest_subarray_members


test_data = [
    (7, [2, 1, 5, 2, 3, 2], 2),
    (7, [2, 1, 5, 2, 8], 1),
    (8, [3, 4, 1, 1, 6], 3),
]


@pytest.mark.parametrize("k, input_array, expected", test_data)
def test_find_averages_of_subarrays(
    k: int, input_array: List[int], expected: int,
):
    # for item in expected:
    assert smallest_subarray_with_given_sum(k, input_array) == expected


# Better Solution
"""
1. First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S’.
2. These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater 
than or equal to ‘S’. We will remember the length of this window as the smallest window so far.
3. After this, we will keep adding one element in the sliding window (i.e. slide the window ahead), in a stepwise fashion.
4. In each step, we will also try to shrink the window from the beginning. We will shrink the window until the window’s sum 
is smaller than ‘S’ again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step we will do two things:
    - Check if the current window length is the smallest so far, and if so, remember its length.
    - Subtract the first element of the window from the running sum to shrink the sliding window.
"""

# The outer for loop runs through every element in the arr and the inner while loop processes each element only once, therefor
# the time complexity will be O(N + N) or O(N). This means that the inner loop is not executed for every i hence the  N + N.
# Space complexity is O(1)
def smallest_subarray_with_given_sum_2(s: int, arr: List) -> int:
    window_start = 0
    minimum_subarray_length = math.inf
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        while current_sum >= s:
            minimum_subarray_length = min(minimum_subarray_length, i - window_start + 1)
            current_sum -= arr[window_start]
            window_start += 1

    if minimum_subarray_length == math.inf:
        return 0
    return minimum_subarray_length


@pytest.mark.parametrize("k, input_array, expected", test_data)
def test_find_averages_of_subarrays_2(
    k: int, input_array: List[int], expected: int,
):
    # for item in expected:
    assert smallest_subarray_with_given_sum_2(k, input_array) == expected
