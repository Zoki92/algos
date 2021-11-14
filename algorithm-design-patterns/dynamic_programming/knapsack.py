import pytest


test_data = [
    ([1, 6, 10, 16], [1, 2, 3, 5], 5, 16),
    ([1, 6, 10, 16], [1, 2, 3, 5], 6, 17),
    ([1, 6, 10, 16], [1, 2, 3, 5], 7, 22),
]


@pytest.mark.parametrize("profits, weights, capacity, expected", test_data)
def test_solve_knapsack(profits, weights, capacity, expected):
    assert solve_knapsack(profits, weights, capacity) == expected


def solve_knapsack(profits, weights, capacity, dp=None):
    n = len(profits)
    if capacity <= 0 or n == 0 or n != len(weights):
        return 0

    dp[:] = [[0 for i in range(capacity + 1)] for y in range(n)]
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            profit2 = dp[i - 1][c]
            dp[i][c] = max(profit1, profit2)
    return dp[n - 1][capacity]


"""
This solution has got time and space complexity of O(N * C) where
N - total items
C - maximum capacity
"""


def print_knapsack_items(dp, profits, weights, capacity):
    n = len(profits)
    print(dp)
    total_profit = dp[n - 1][capacity]
    items = []
    for i in range(n - 1, 0, -1):
        if total_profit != dp[i - 1][capacity]:
            capacity -= weights[i]
            total_profit -= profits[i]
            items.append(weights[i])

    return items


if __name__ == "__main__":
    dp = []
    solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5, dp=dp)
    items = print_knapsack_items(dp, [1, 6, 10, 16], [1, 2, 3, 5], 5)
    print(items)
