"""
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. 
Our goal is to find out if there is a free interval that is common to all employees. You can assume 
that each list of employee working hours is sorted on the start time.

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employess are free between [3,5].

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employess are free between [4,6] and [8,9].

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employess are free between [5,7].
"""
from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        return self.interval.start < other.interval.start

    def __repr__(self):
        return f"{self.interval}, {self.employeeIndex}, {self.intervalIndex}"


"""
Time complexity #

The time complexity of the above algorithm is O(N∗logK), where ‘N’ is the total number of intervals and ‘K’ is
the total number of employees. This is due to the fact that we are iterating through the intervals only once (which will take O(N)), 
and every time we process an interval, we remove (and can insert) one interval in the Min Heap, (which will take O(logK)). 
At any time the heap will not have more than ‘K’ elements.

Space complexity #

The space complexity of the above algorithm will be O(K) as at any time the heap will not have more than ‘K’ elements.

"""


def find_employee_free_time(schedule):
    if schedule is None:
        return []
    n = len(schedule)
    result, min_heap = [], []
    # [Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]
    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    # heap = [([1, 3], 0, 0), ([2, 3], 1, 0)]
    previos_interval = min_heap[0].interval
    while min_heap:

        queue_top = heappop(min_heap)
        if previos_interval.end < queue_top.interval.start:
            result.append(Interval(previos_interval.end, queue_top.interval.start))
            previos_interval = queue_top.interval
        else:
            if previos_interval.end < queue_top.interval.end:
                previos_interval = queue_top.interval

        employee_schedule = schedule[queue_top.employeeIndex]
        if len(employee_schedule) > queue_top.intervalIndex + 1:
            heappush(
                min_heap,
                EmployeeInterval(
                    employee_schedule[queue_top.intervalIndex + 1],
                    queue_top.employeeIndex,
                    queue_top.intervalIndex + 1,
                ),
            )
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    # print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    # input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    # print("Free intervals: ", end="")
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()

    # input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    # print("Free intervals: ", end="")
    # for interval in find_employee_free_time(input):
    #     interval.print_interval()
    # print()


main()
