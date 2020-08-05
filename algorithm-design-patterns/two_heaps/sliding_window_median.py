"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2] -> median is 1.5
[2, -1] -> median is 0.5
[-1, 3] -> median is 1.0
[3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
"""

from heapq import *
import heapq


# The full time complexity will be O(n * k) where n is the total number of elements in the input array
# and k is the size of the sliding window. We are going through each element and we are doing:
# - Inserting and removing numbers from heaps of size K, that's O(logn)
# - Removing the element going out of the slide window, this will tak O(K) as we will be searching this
# element in the array of size K, the heap
# Space complexity is O(k) ignoring the resulting array
class SlidingWindowMedian:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]

        for i in range(0, len(nums)):
            if not self.max_heap or -self.max_heap[0] >= nums[i]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k + 1] = -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
                else:
                    result[i - k + 1] = -self.max_heap[0] / 1.0

                element_to_be_removed = nums[i - k + 1]

                if element_to_be_removed <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element_to_be_removed)
                else:
                    self.remove(self.min_heap, element_to_be_removed)

                self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        # find element
        ind = heap.index(element)
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]

        # we can use heapify to readjust the elements but that would be O(n)
        # instead, we will just adjust only one element which will be O(logn)
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def rebalance_heaps(self):

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
