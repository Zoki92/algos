"""
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
The cost of connecting two ropes is equal to the sum of their lengths.

Example 1:

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

Example 2:

Input: [3, 4, 5, 6]
Output: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

Example 3:

Input: [1, 3, 11, 5, 2]
Output: 42
Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
"""
import pytest
from typing import List
from heapq import *


# Given ‘N’ ropes, we need O(N∗logN) to insert all the ropes in the heap.
# In each step, while processing the heap, we take out two elements from the heap and insert one.
# This means we will have a total of ‘N’ steps, having a total time complexity of O(N∗logN)
# The space complexity will be O(N) because we need to store all the ropes in the heap.
def minimum_cost_to_connect_ropes(rope_lengths: List[int]) -> int:
    min_heap = []
    for length in rope_lengths:
        heappush(min_heap, length)

    result, temp = 0, 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)
    return result


test_data = [
    ([1, 3, 11, 5], 33),
    ([3, 4, 5, 6], 36),
    ([1, 3, 11, 5, 2], 42),
]


@pytest.mark.parametrize("rope_lengths, expected", test_data)
def test_minimum_cost_to_connect_ropes(rope_lengths, expected):
    assert minimum_cost_to_connect_ropes(rope_lengths) == expected
