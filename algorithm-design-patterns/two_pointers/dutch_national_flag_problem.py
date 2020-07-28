"""Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat 
numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our 
input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

"""
import pytest
from typing import List


"""
We can use a Two Pointers approach while iterating through the array. Let’s say the two 
pointers are called low and high which are pointing to the first and the last element of the array respectively. 
So while iterating, we will move all 0s before low and all 2s after high so that in the end, 
all 1s will be between low and high.
"""

# The time complexity of the above algorithm will be O(N) as we are iterating the input array only once
# Space is O(1)
def dutch_flag_sort(arr: List[int]) -> List[int]:
    low = 0
    high = len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    return arr


test_data = [
    ([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
    ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_dutch_flag_sort(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert dutch_flag_sort(arr) == expected

