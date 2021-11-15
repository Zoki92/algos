from typing import List

import pytest


def equal_sum_sets_brute(num: List[int]) -> bool:
    """
    Given a set of positive numbers, find if we can partition it into two subsets such that the sum of the elements
    in both subsets is equal.
    """
    ret = False
    # for each number i
    # create a new set which includes that number if it doesn't exceed S/2, and recursevely process the remaining numbers
    # create a new set which doesn't include that number and recursevly process the remaining items
    # return True if any of the above sets has a sum equal to S/2 otherways return false
    s = sum(num)
    if s % 2 != 0:
        return False
    # initialise the dp array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for x in range(int(s / 2) + 1)] for y in range(len(num))]
    return True if recursion_helper(dp, num, int(s / 2), 0) == 1 else False


def recursion_helper(dp, num, sum, current_index):
    # base check
    if sum == 0:
        return True
    n = len(num)
    if n == 0 or current_index >= n:
        return 0

    # if we have not already processed similar problem
    if dp[current_index][sum] == -1:
        # recursive call after choosing the number at the current index
        # if the number at the current index exceeds sum, it shouldn't be processed
        if num[current_index] <= sum:
            if (
                recursion_helper(dp, num, sum - num[current_index], current_index + 1)
                == 1
            ):
                dp[current_index][sum] = 1
                return 1
    # recursive call after excluding the number at current index
    dp[current_index][sum] = recursion_helper(dp, num, sum, current_index + 1)
    return dp[current_index][sum]


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
