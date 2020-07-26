"""
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

"""
import pytest
from typing import List


def make_squares(arr: List[int]) -> List[int]:
    squares = [0 for _ in range(len(arr))]
    left, right = 0, len(arr) - 1
    filled = right
    while left < right:
        if arr[left] ** 2 >= arr[right] ** 2:
            squares[filled] = arr[left] ** 2
            squares[filled - 1] = arr[right] ** 2
        else:
            squares[filled] = arr[right] ** 2
            squares[filled - 1] = arr[left] ** 2

        right -= 1
        left += 1
        filled -= 2

    return squares


test_data = [
    ([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),
    ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_make_squares(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert make_squares(arr) == expected


# Time complexity is O(N) and space complexity is O(N)
def make_squares_2(arr: List[int]) -> List[int]:
    arr_length = len(arr)
    squares = [0 for _ in range(arr_length)]
    highest_squared = arr_length - 1
    left, right = 0, arr_length - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            squares[highest_squared] = left_square
            left += 1
        else:
            squares[highest_squared] = right_square
            right -= 1

        highest_squared -= 1

    return squares


@pytest.mark.parametrize("arr, expected", test_data)
def test_make_squares_2(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert make_squares_2(arr) == expected
