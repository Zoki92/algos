import pytest


def count_of_subset_sum(num, s):
    """
    Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number S

    Time and space complexity is O(N * S) where N is the total number and S is the sum
    """
    n = len(num)
    dp = [[-1 for _ in range(s + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for j in range(1, s + 1):
        dp[0][j] = 1 if num[0] == j else 0

    for i in range(1, n):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if num[i] <= j:
                dp[i][j] += dp[i - 1][j - num[i]]
    return dp[n - 1][s]


def count_of_subset_sum_improved(num, s):
    """
    Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number S

    Time complexity is O(N * S) where N is the total number and S is the sum
    Space complexity is O(S) where S is the sum
    """
    dp = [0 for x in range(s + 1)]
    dp[0] = 1

    for n in num:
        for y in range(s, -1, -1):
            if n <= y:
                dp[y] += dp[y - n]
    return dp[s]


@pytest.mark.parametrize(
    ("input", "sum", "expected"),
    (
        ([1, 1, 2, 3], 4, 3),
        ([1, 2, 7, 1, 5], 9, 3),
    ),
)
def test_count_of_subset_sum(input, sum, expected):
    assert count_of_subset_sum_improved(input, sum) == expected
