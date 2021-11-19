import pytest


def count_of_subset_sum(num, s):
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
