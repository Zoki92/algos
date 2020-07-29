"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all
necessary intervals to produce a list that has only mutually exclusive intervals.

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""
import pytest
from typing import List


def insert(intervals, new_interval):
    merged = []

    i, start, end = 0, 0, 1
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


test_data = [
    ([[1, 3], [5, 7], [8, 12]], [4, 6], [[1, 3], [4, 7], [8, 12]]),
    ([[1, 3], [5, 7], [8, 12]], [4, 10], [[1, 3], [4, 12]]),
    ([[2, 3], [5, 7]], [1, 4], [[1, 4], [5, 7]]),
]


@pytest.mark.parametrize("arr, interval, expected", test_data)
def test_insert(
    arr: List[List[int]], interval: List[int], expected: List[List[int]],
):
    # for item in expected:
    assert insert(arr, interval) == expected

