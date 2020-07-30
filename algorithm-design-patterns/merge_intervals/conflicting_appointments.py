"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
"""
import pytest
from typing import List

# this works
def can_attend_all_appointments_2(intervals: List[int]) -> int:
    intervals.sort(key=lambda x: x[0])
    i, start, end = 1, 0, 1
    interval = intervals[0]
    while i < len(intervals):
        # we have an overlap
        if interval[end] >= intervals[i][start] and interval[end] <= intervals[i][end]:
            return False
        interval = intervals[i]
        i += 1
    return True


# The time complexity of the above algorithm is O(N∗logN) where ‘N’ is the total number of appointments.
# Though we are iterating the intervals only once, our algorithm will take O(N∗logN) since we need to sort them in the beginning.
# Space complexity is O(N) needed for sorting
def can_attend_all_appointments(intervals: List[int]) -> int:
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        # have overlap
        if intervals[i][start] <= intervals[i - 1][end]:
            return False
    return True


test_data = [
    ([[1, 4], [2, 5], [7, 9]], False),
    ([[6, 7], [2, 4], [8, 12]], True),
    ([[4, 5], [2, 3], [3, 6]], False),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_can_attend_all_appointments(
    arr: List[List[int]], expected: bool,
):
    # for item in expected:
    assert can_attend_all_appointments(arr) == expected


can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])
