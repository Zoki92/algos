from typing import List

import pytest


def equal_sum_sets_brute(numbers: List[int]) -> bool:
    """
    Given a set of positive numbers, find if we can partition it into two subsets such that the sum of the elements
    in both subsets is equal.
    """
    ret = False
    # for each number i
    # create a new set which includes that number if it doesn't exceed S/2, and recursevely process the remaining numbers
    # create a new set which doesn't include that number and recursevly process the remaining items
    # return True if any of the above sets has a sum equal to S/2 otherways return false
    condition_sum = sum(numbers)
    if condition_sum % 2 != 0:
        return False
    return recursion_helper(condition_sum / 2, numbers, 0)


def recursion_helper(cond_sum, numbers, current_index):
    if cond_sum == 0:
        return True
    n = len(numbers)
    if n == 0 or current_index >= n:
        return False
    if numbers[current_index] <= cond_sum:
        if recursion_helper(
            cond_sum - numbers[current_index], numbers, current_index + 1
        ):
            return True
    return recursion_helper(cond_sum, numbers, current_index + 1)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 2, 3, 4], True),
        ([1, 1, 3, 4, 7], True),
        ([2, 3, 4, 6], False),
    ],
)
def test_equal_sum_sets_brute(input, expected):
    assert equal_sum_sets_brute(input) == expected
