import pytest


def count_of_subset_sum(num, s):
    """
    Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number S

    A basic brute force solution is to try all subsets of the given numbers to count the subsets that have
    a sum equal to S.

    for each number 'i'
    create a new set which includes number 'i' if it does not exceed 'S', and recursively
        process the remaining numbers and sum
    create a new set without number 'i', and recursively process the remaining numbers
    return the count of subsets who has a sum equal to 'S'

    The time complexity is O(2^n) where n is the total number
    The space complexity is O(N) where n is the count of method calls on the stack
    """
    return recursion_helper(num, s, 0)


def recursion_helper(num, s, current_index):
    if s == 0:
        return 1
    n = len(num)
    if n == 0 or current_index >= n:
        return 0

    sum1 = 0
    if num[current_index] <= s:
        sum1 = recursion_helper(num, s - num[current_index], current_index + 1)
    sum2 = recursion_helper(num, s, current_index + 1)
    return sum1 + sum2


@pytest.mark.parametrize(
    ("input", "sum", "expected"),
    (
        ([1, 1, 2, 3], 4, 3),
        ([1, 2, 7, 1, 5], 9, 3),
    ),
)
def test_count_of_subset_sum(input, sum, expected):
    assert count_of_subset_sum(input, sum) == expected
