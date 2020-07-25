"""Given an array of characters where each character represents a fruit tree you are given two baskets and your goal is to put
the maximum number of fruits in each of basket.The only restriction is that each basket can only have one type of fruit.
You can start with any tree but once you started you cannot skip a tree.
Write a function that returns the maximum number of fruits in both the baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
"""
from collections import defaultdict
import pytest
from typing import List


def fruits_into_baskets(fruits: List) -> int:
    window_start = 0
    max_fruits = 0
    hash_map = defaultdict(int)

    for window_end in range(len(fruits)):
        current_fruit = fruits[window_end]

        if len(hash_map) == 2 and current_fruit not in hash_map:
            max_fruits = max(max_fruits, sum(hash_map.values()))
            del hash_map[fruits[window_start]]
            window_start += 1
        hash_map[current_fruit] += 1
        max_fruits = max(max_fruits, sum(hash_map.values()))
    return max_fruits


test_data = [
    (["A", "B", "C", "A", "C"], 3),
    (["A", "B", "C", "B", "B", "C"], 5),
]


@pytest.mark.parametrize("input_array, expected", test_data)
def test_fruits_into_baskets(
    input_array: List[int], expected: int,
):
    # for item in expected:
    assert fruits_into_baskets(input_array) == expected


"""
The trick here is that we go loop through the fruit array and collect the fruit inside a dict.
Now we calculate maximum unles we get 3 items in the dict. In this case we remove the window_start item
because it cannot be included in the calculation. Once it's removed only then we calculate the  max.
the max is calculated with window_end - window_start + 1 (list starts with 0 index hence the 1).
The window start only increases if we have 3 distinct fruits so, for the case "C", "A", "C", it won't move
until we get new fruit type hence, 2 - 0 + 1 = 3
"""


# The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input array.
# The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.
def fruits_into_baskets_2(fruits: List) -> int:
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


test_data = [
    (["A", "B", "C", "A", "C"], 3),
    (["A", "B", "C", "B", "B", "C"], 5),
]


@pytest.mark.parametrize("input_array, expected", test_data)
def test_fruits_into_baskets_2(
    input_array: List[int], expected: int,
):
    # for item in expected:
    assert fruits_into_baskets_2(input_array) == expected

