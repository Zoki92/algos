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

    The time complexity of this algorithm is O(N * S) where n is the number of items and S is the sum
    The space complexity is O(S), S same as above
    """
    n = len(numbers)
    dp = [False for i in range(sum + 1)]
    dp[0] = True

    for num in numbers:
        for i in range(sum, -1, -1):
            # if dp[i] == true this means we can get the sum without num[i] hence we can move on to the next number
            # else we can include num[i] and see if we can  find a subset to get the remaining sum
            if not dp[i] and sum >= num:
                dp[i] = dp[i - num]

            # another approach that works
            # if num <= i:
            #     dp[i] = dp[i] or dp[i - num]

    return dp[sum]


@pytest.mark.parametrize(
    ("input_numbers", "sum", "expected"),
    (
        ((1, 2, 3, 7), 6, True),
        ((1, 2, 7, 1, 5), 10, True),
        ((1, 3, 4, 8), 6, False),
        ((1,), 1, True),
        ((2,), 1, False),
    ),
)
def test_subset_sum(input_numbers, sum, expected):
    assert subset_sum(input_numbers, sum) == expected
