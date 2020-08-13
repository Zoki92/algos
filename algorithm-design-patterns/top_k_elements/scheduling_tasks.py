"""
You are given a list of tasks that need to be run, in any order, on a server. 
Each task will take one CPU interval to execute but once a task has finished, 
it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, 
find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a

Example 2:

Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
"""
import pytest
from heapq import *


# The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of tasks. Our while loop will
# iterate once for each occurrence of the task in the input (i.e. ‘N’) and in each iteration we will remove a task
# from the heap which will take O(logN) time. Hence the overall time complexity of our algorithm is O(N*logN).
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ tasks in the HashMap.
def schedule_tasks(tasks, k):
    interval_count = 0
    task_frequency = {}
    for task in tasks:
        task_frequency[task] = task_frequency.get(task, 0) + 1
    max_heap = []
    for task, freq in task_frequency.items():
        heappush(max_heap, (-freq, task))

    while max_heap:
        wait_list = []
        n = k + 1  # try to execute as many as k + 1 tasks from the max-heap
        while n > 0 and max_heap:
            interval_count += 1
            freq, char = heappop(max_heap)
            if -freq > 1:
                # decrement the freq and add to the waitlist
                wait_list.append((freq + 1, char))
            n -= 1

            # put all the waiting list back to the heap       for freq, char in wait_list:
            heappush(max_heap, (freq, char))

        if max_heap:
            # we will be having n idle intervals for the next iteration
            interval_count += n

    return interval_count


test_data = [
    (["a", "a", "a", "b", "c", "c"], 2, 7),
    (["a", "b", "a"], 3, 5),
]


@pytest.mark.parametrize("tasks, k, expected", test_data)
def test_schedule_tasks(tasks, k, expected):
    assert schedule_tasks(tasks, k) == expected
