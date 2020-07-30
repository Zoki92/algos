"""Given a list of intervals representing the start and end time of ‘N’ meetings, 
find the minimum number of rooms required to hold all the meetings.

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
hold all the meetings.

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

"""
import pytest
from typing import List
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __str__(self):
        return f"[{self.start},{self.end}]"

    def __repr__(self):
        return f"[{self.start},{self.end}]"


"""
The time complexity of the above algorithm is O(N∗logN), where ‘N’ is the total number of meetings.
This is due to the sorting that we did in the beginning. Also, while iterating the meetings we might need
to poll/offer meeting to the priority queue. Each of these operations can take O(logN). 
Overall our algorithm will take O(NlogN)

The space complexity of the above algorithm will be O(N) which is required for sorting. 
Also, in the worst case scenario, we’ll have to insert all the meetings into the Min Heap 
(when all meetings overlap) which will also take O(N)O(N)O(N) space. The overall space complexity of our algorithm is O(N).
"""


def min_meeting_rooms(meetings: List[List[int]]) -> int:
    # [2, 3], [2, 4], [3, 5], [4, 5]
    # [1, 4], [2, 5], [7, 9]
    meetings.sort(key=lambda x: x.start)
    min_rooms = 0
    min_heap = []

    for meeting in meetings:
        print(min_heap)
        # remove all the meetings that have ended
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)

        # add the current meeting into min heap
        heappush(min_heap, meeting)

        # all active meetings are in the min heap so we need rooms for all of them
        min_rooms = max(min_rooms, len(min_heap))
    print("___________________-")
    return min_rooms


test_data = [
    ([[1, 4], [2, 5], [7, 9]], 2),
    ([[6, 7], [2, 4], [8, 12]], 1),
    ([[1, 4], [2, 3], [3, 6]], 2),
    ([[4, 5], [2, 3], [2, 4], [3, 5]], 2),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_min_meeting_rooms(
    arr: List[List[int]], expected: int,
):
    # for item in expected:
    assert min_meeting_rooms(arr) == expected


def main():
    print(
        "Minimum meeting rooms required: "
        + str(
            min_meeting_rooms(
                [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
            )
        )
    )
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))
    )
    print(
        "Minimum meeting rooms required: "
        + str(
            min_meeting_rooms(
                [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
            )
        )
    )


main()
