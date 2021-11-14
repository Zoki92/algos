from typing import List

import pytest

test_data = [
    ([1, 6, 10, 16], [1, 2, 3, 5], 5, 16),
    ([1, 6, 10, 16], [1, 2, 3, 5], 6, 17),
    ([1, 6, 10, 16], [1, 2, 3, 5], 7, 22),
]


@pytest.mark.parametrize("profits, weights, capacity, expected", test_data)
def test_solve_knapsack(profits, weights, capacity, expected):
    assert solve_knapsack(profits, weights, capacity) == expected


"""
The space complexity of this algorithm is O(C) where C is the knapsack maximum capacity
The time complexity is O(N * C), N is number of items, C like above
"""


def solve_knapsack(profits: List[int], weights: List[int], capacity: int) -> int:

    n = len(weights)
    if capacity <= 0 or n == 0 or n != len(weights):
        return 0

    dp = [0 for i in range(capacity + 1)]

    # if we have only one weight we will take it if it is not more than the capacity
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(n):
        # going backwards on this will ensure that once the value for dp[c] is processed you will not override it
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[c - weights[i]]
            profit2 = dp[c]
            dp[c] = max(profit1, profit2)

    return dp[capacity]
