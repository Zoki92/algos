"""Given an array of intervals, find the next interval of each interval. In a list of intervals, 
for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval. 
If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

Input: Intervals [[2,3], [3,4], [5,6]]
Output: [1, 2, -1]
Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, 
the next interval of [3,4] is [5,6] having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.

Input: Intervals [[3,4], [1,5], [4,6]]
Output: [2, -1, -1]
Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. There is no next interval for [1,5] and [4,6].
"""
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


#   The time complexity of our algorithm will be O(NlogN) where ‘N’ is the total number of intervals.
# The space complexity will be O(N) because we will be storing all the intervals in the heaps.
def find_next_interval(intervals):
    n = len(intervals)
    max_start_heap, max_end_heap = [], []
    result = [0 for _ in range(n)]
    for end_index in range(n):
        heappush(max_start_heap, (-intervals[end_index].start, end_index))
        heappush(max_end_heap, (-intervals[end_index].end, end_index))

    for _ in range(n):
        top_end, end_index = heappop(max_end_heap)
        result[end_index] = -1

        if -max_start_heap[0][0] >= -top_end:
            top_start, start_index = heappop(max_start_heap)

            # top_start, start_index = -5 , 2
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, start_index = heappop(max_start_heap)
            result[end_index] = start_index
            heappush(max_start_heap, (top_start, start_index))
    return result


def main():

    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    # print("Next interval indices are: " + str(result))

    # result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    # print("Next interval indices are: " + str(result))


main()

