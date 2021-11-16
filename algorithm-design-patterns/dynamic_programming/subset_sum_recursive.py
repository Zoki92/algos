from typing import List

import pytest


def subset_sum(numbers: List[int], sum: int) -> bool:
    """
    Given a set of positive numbers determine if a subset exists whose sum is equal to a given number S
    Brute force solution
    for each number i
    create a new set which includes number i if it doesn't exceed S and recursively process the remaining numbers
    create a new set without the number i and recursively process the remaining numbers
    return true if any of the above two sets had a sum equal to S otherwise return false
    """
    result = False
    if len(numbers) == 1 and numbers[0] == sum:
        return True
    result = recursion_helper(numbers, sum, 0)
    return result


def recursion_helper(numbers, sum, current_index):
    # base check
    if sum == 0:
        return True

    n = len(numbers)
    if n == 0 or current_index >= n:
        return False

    # if the number is greater than the sum then we cannot process it
    if numbers[current_index] <= sum:
        if recursion_helper(numbers, sum - numbers[current_index], current_index + 1):
            return True
    # recursive call after exluding the number at the current index
    return recursion_helper(numbers, sum, current_index + 1)


@pytest.mark.parametrize(
    ("input_numbers", "sum", "expected"),
    (
        ((1, 2, 3, 7), 6, True),
        ((1, 2, 7, 1, 5), 10, True),
        ((1, 3, 4, 8), 6, False),
    ),
)
def test_subset_sum(input_numbers, sum, expected):
    assert subset_sum(input_numbers, sum) == expected
