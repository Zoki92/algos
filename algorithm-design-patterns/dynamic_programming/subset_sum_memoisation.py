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

    The time and space complexity is O(N * S) where N represents total numbers and S is sum
    """
    result = False
    if len(numbers) == 1 and numbers[0] == sum:
        return True
    dp = [[-1 for x in range(sum + 1)] for y in range(len(numbers))]
    result = recursion_helper(dp, numbers, sum, 0)
    return True if result == 1 else False


def recursion_helper(dp, numbers, sum, current_index):
    # base check
    if sum == 0:
        return True

    n = len(numbers)
    if n == 0 or current_index >= n:
        return False

    # if we have not yet processed that problem
    if dp[current_index][sum] == -1:
        # recursive call after choosing the number at the current index
        # if the number at the current index exceeds the sum we shouldn't process this
        if numbers[current_index] <= sum:
            if recursion_helper(
                dp, numbers, sum - numbers[current_index], current_index + 1
            ):
                dp[current_index][sum] = 1
                return 1
        # recursive call after exluding the number at the current index
        dp[current_index][sum] = recursion_helper(dp, numbers, sum, current_index + 1)
    return dp[current_index][sum]


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
