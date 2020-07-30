"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. 
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.


Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
"""


from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        self.end < other.end


"""
Time complexity #

The time complexity of the above algorithm is O(N∗logN) where ‘N’ is the total number of jobs. This is due 
to the sorting that we did in the beginning. Also, while iterating the jobs, we might need to poll/offer 
jobs to the priority queue. Each of these operations can take O(logN)O(logN)O(logN). Overall our algorithm will take O(NlogN).

Space complexity #

The space complexity of the above algorithm will be O(N), which is required for sorting. Also, in the worst case, 
we have to insert all the jobs into the priority queue (when all jobs overlap) which will also take O(N) space. 
The overall space complexity of our algorithm is O(N)O(N)O(N).
"""


def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    min_heap = []
    for j in jobs:
        # remove all the jobs that have ended
        while len(min_heap) > 0 and j.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load

    return -1


def main():
    print(
        "Maximum CPU load at any time: "
        + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)]))
    )
    print(
        "Maximum CPU load at any time: "
        + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)]))
    )
    print(
        "Maximum CPU load at any time: "
        + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)]))
    )


main()
