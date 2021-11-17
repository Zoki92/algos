from typing import List
import pytest


def minimum_subset_difference(numbers: List[int]) -> int:
    """
    Let's assume that S1 and S2 are the two desired subsets. A basic brute force solution could be to try adding
    each element into S1 or S2 in order to find the combination that gives the minimum sum difference between the two sets.

    for each number i
        add number i to s1 and recursively process the remaining numbers
        add number i to s2 and recursively process the remaining numbers
    return the minimum absolute difference of the two above sets

    The time complexity of this algorithm is O(2^n) where n is the total number
    The space complexity is O(n) which is required to store the recursion stack
    """
    result = None
    result = recursion_helper(numbers, 0, 0, 0)
    return result


def recursion_helper(numbers, current_index, sum1, sum2):
    if len(numbers) == current_index:
        return abs(sum1 - sum2)

    diff1 = recursion_helper(
        numbers, current_index + 1, sum1 + numbers[current_index], sum2
    )
    diff2 = recursion_helper(
        numbers, current_index + 1, sum1, sum2 + numbers[current_index]
    )

    return min(diff1, diff2)


def minimum_subset_difference_memoised(numbers: List[int]) -> int:
    """
    The time and space complexity is O(N*S) where N is the total numbers, and S is the sum of the numbers
    """
    s = sum(numbers)
    dp = [[-1 for x in range(s + 1)] for y in range(len(numbers))]
    return recursion_helper_memoised(dp, numbers, 0, 0, 0)


def recursion_helper_memoised(dp, numbers, current_index, sum1, sum2):
    if current_index == len(numbers):
        return abs(sum1 - sum2)

    if dp[current_index][sum1] == -1:
        diff1 = recursion_helper_memoised(
            dp, numbers, current_index + 1, sum1 + numbers[current_index], sum2
        )
        diff2 = recursion_helper_memoised(
            dp, numbers, current_index + 1, sum1, sum2 + numbers[current_index]
        )
        dp[current_index][sum1] = min(diff1, diff1)
    return dp[current_index][sum1]


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


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([1, 2, 3, 9], 3),
        ([1, 2, 7, 1, 5], 0),
        ([1, 3, 100, 4], 92),
    ),
)
def test_minimum_subset_difference_memoised(input, expected):
    assert minimum_subset_difference_memoised(input) == expected
