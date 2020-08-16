"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
import pytest
from typing import List


def max_profit(prices: List[int]) -> int:
    buy_index = 0
    max_profit = 0
    for i in range(len(prices)):
        if prices[buy_index] < prices[i]:
            current_profit = prices[i] - prices[buy_index]
            max_profit = max(max_profit, current_profit)
        else:
            buy_index = i
    return max_profit


test_data = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
]


@pytest.mark.parametrize("prices, expected", test_data)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
