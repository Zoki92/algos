"""Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint
intervals sorted on their start time.

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""
import pytest
from typing import List


def merge2(intervals_a: List[int], intervals_b: List[int]) -> List[int]:
    result = []
    i, start, end = 0, 0, 1
    while i < len(intervals_a):
        interval_a = intervals_a[i]
        for j in range(len(intervals_b)):
            interval_b = intervals_b[j]
            if interval_a[end] == interval_b[end]:
                result.append(
                    [max(interval_a[start], interval_b[start]), interval_b[end]]
                )
            elif interval_a[start] == interval_b[start]:
                result.append(
                    [interval_b[start], min(interval_b[end], interval_a[end])]
                )
            elif interval_a[start] == interval_b[end]:
                result.append([interval_a[start], interval_b[end]])
            elif interval_a[start] <= interval_b[end] <= interval_a[end]:
                result.append(
                    [
                        max(interval_a[start], interval_b[start],),
                        min(interval_a[end], interval_b[end]),
                    ]
                )
        i += 1
    return result


# As we are iterating through both the lists once, the time complexity of the above
# algorithm is O(N+M) where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.
# Ignoring the space needed for the result list the algorithm runs in O(1)
def merge(intervals_a: List[int], intervals_b: List[int]) -> List[int]:
    result = []
    i, j, start, end = 0, 0, 0, 1
    while i < len(intervals_a) and j < len(intervals_b):
        a_overlaps_b = (
            intervals_a[i][start] >= intervals_b[j][start]
            and intervals_a[i][start] <= intervals_b[j][end]
        )
        b_overlaps_a = (
            intervals_b[j][start] >= intervals_a[i][start]
            and intervals_b[j][start] <= intervals_a[i][end]
        )
        if a_overlaps_b or b_overlaps_a:
            result.append(
                [
                    max(intervals_a[i][start], intervals_b[j][start]),
                    min(intervals_a[i][end], intervals_b[j][end]),
                ]
            )

        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1
    return result


test_data = [
    ([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]], [[2, 3], [5, 6], [7, 7]],),
    ([[1, 3], [5, 7], [9, 12]], [[5, 10]], [[5, 7], [9, 10]],),
]


@pytest.mark.parametrize("arr, interval, expected", test_data)
def test_merge(
    arr: List[List[int]], interval: List[int], expected: List[List[int]],
):
    # for item in expected:
    assert merge(arr, interval) == expected
