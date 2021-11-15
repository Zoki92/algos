from typing import List

import pytest


def equal_sum_sets(numbers: List[int]) -> bool:
    """
    Given a set of positive numbers, find if we can partition it into two subsets such that the sum of the elements
    in both subsets is equal.

    The time and space complexity for this is O(N * S) where N is the total number of numbers in the set, and S is the sum of the numbers
    """
    s = sum(numbers)
    if s % 2 != 0:
        return False

    s = int(s / 2)
    n = len(numbers)
    dp = [[False for i in range(s + 1)] for y in range(n)]

    # populate the s=0 columns, as we can always for 0 sum with an empty set
    for i in range(n):
        dp[i][0] = True

    # with only one number we can form a subset only when the required sum is equal to its value
    for j in range(1, s + 1):
        dp[0][j] = numbers[0] == j

    # process all subsets for all sum
    for i in range(1, n):
        for j in range(1, s + 1):
            # if we can get the sum j without the number at index i
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            # else if we can find a subset to get the remaining sum
            elif j >= numbers[i]:
                dp[i][j] = dp[i - 1][j - numbers[i]]

    # the bottom right corner will have the answer
    return dp[n - 1][s]


def equal_sum_sets_improved(numbers):
    """
    Given a set of positive numbers, find if we can partition it into two subsets such that the sum of the elements
    in both subsets is equal.

    The time complexity for this is O(N * S) where N is the total number of numbers in the set, and S is the sum of the numbers
    The space complexity is O(S) where S is like above
    """
    s = sum(numbers)
    if s % 2 != 0:
        return False

    s = int(s / 2)
    n = len(numbers)
    dp = [False for i in range(s + 1)]
    dp[0] = True

    for num in numbers:
        for s in range(s, -1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[s]


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 2, 3, 4], True),
        ([1, 1, 3, 4, 7], True),
        ([2, 3, 4, 6], False),
    ],
)
def test_equal_sum_sets(input, expected):
    assert equal_sum_sets(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 2, 3, 4], True),
        ([1, 1, 3, 4, 7], True),
        ([2, 3, 4, 6], False),
    ],
)
def test_equal_sum_sets_improved(input, expected):
    assert equal_sum_sets_improved(input) == expected
