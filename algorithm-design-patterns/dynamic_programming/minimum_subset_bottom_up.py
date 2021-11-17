from typing import List
import pytest


def minimum_subset_difference(numbers: List[int]) -> int:
    """
    Let's assume that S represents the total sum of all the numbers. So in this problem we are trying to find a subset
    whose sum is as close to S/2.

    So once we process all subsets, if it's not possible to find subset with such sum then we get the subset whose sum is closest
    to the solution. This means that the total sum minus this sum will give us the other subset sum, and after we can get the absolute
    of their difference to calculate the minimum subset difference.

    The time and space complexity of this algorithm is O(N * C), where N is the total number of items and C is the sum of all the numbers
    """
    s = sum(numbers)
    n = len(numbers)
    dp = [[False for i in range(s // 2 + 1)] for y in range(n)]

    # populate the s=0 columns as we can always form 0 sum with an empty set
    for i in range(n):
        dp[i][0] = True

    # with only one number we can form a subset only when the required sum is equal to that number
    for j in range(0, s // 2 + 1):
        dp[0][j] = numbers[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, s // 2 + 1):
            # if we can get the sum without the number at index i
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= numbers[i]:
                dp[i][j] = dp[i - 1][j - numbers[i]]

    sum1 = 0
    for i in range(s // 2, -1, -1):
        if dp[n - 1][i]:
            sum1 = i
            break
    sum2 = s - sum1
    return abs(sum2 - sum1)


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([1, 2, 3, 9], 3),
        ([1, 2, 7, 1, 5], 0),
        ([1, 3, 100, 4], 92),
    ),
)
def test_minimum_subset_difference(input, expected):
    assert minimum_subset_difference(input) == expected
