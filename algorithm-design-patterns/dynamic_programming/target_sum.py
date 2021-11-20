import pytest


def find_target_subset(num, s):
    """
    You are given a set of positive numbers and a target sum S. Each number should be assigned either a + or -
    sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target S

    {1,1,2,3} S=1
    The give set has 3 ways to make a sum of 1
    {+1 - 1 -2 +3} {-1+1-2+3} {+1+1+2-3}

    Solution:
    We are asked to find two subsets of the given numbers whose difference is equal to the given target S.
    So for solution 1 from above, the two subsets are {1, 3} = s1 and {1, 2} = s2, S=1

    Sum(s1) - Sum(s2) = S

    Let's assume that Sum(num) denotes the total sum of all the numbers

    Sum(s1) + Sum(s2) = Sum(num)

    Let's add the above two equations:

    Sum(s1) - Sum(s2) + Sum(s1) + Sum(s2) = S + Sum(num)

    Sum(s1) = (S + Sum(num)) / 2 ----> (1)

    Which means that one of the set s1, has a sum equal to  (1). This essentially converts our problem to:
    Find the count of subsets of the given numbers whose sum is equal to (S + Sum(num)) / 2

    Time and space complexity is O(N * C) where N is the total numbers and S is the desired sum.
    """
    total_sum = sum(num)

    if (s + total_sum) % 2 == 1:
        return 0

    n = len(num)
    the_sum = (s + total_sum) // 2
    dp = [[0 for _ in range(the_sum + 1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, the_sum + 1):
        dp[0][i] = 1 if num[0] == i else 0

    for i in range(1, n):
        for j in range(1, the_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if num[i] <= j:
                dp[i][j] += dp[i - 1][j - num[i]]

    return dp[n - 1][the_sum]


def find_target_subset_optimized(num, s):
    total_sum = sum(num)

    if (s + total_sum) % 2 == 1:
        return 0

    n = len(num)
    the_sum = (s + total_sum) // 2

    dp = [0 for _ in range(the_sum + 1)]
    dp[0] = 1

    for s in range(1, the_sum + 1):
        dp[s] = 1 if num[0] == s else 0

    for i in range(1, n):
        for j in range(the_sum, -1, -1):
            if j >= num[i]:
                dp[j] += dp[j - num[i]]

    return dp[the_sum]


@pytest.mark.parametrize(
    ("input, sum, expected"),
    (
        ([1, 1, 2, 3], 1, 3),
        ([1, 2, 7, 1], 9, 2),
    ),
)
def test_find_target_subset(input, sum, expected):
    assert find_target_subset_optimized(input, sum) == expected
