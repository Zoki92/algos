"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
"""
from heapq import *


# we store the items in the max heap as negative because by default heap stores the smallest value
# is kept inside heap[0], therefore keeping the value as negative will be kept on such position
# we insert num in max heap if the number is smaller than the largest number in the heap
# exam: [-3, -1]  so ideally we have max_heap = [1, 3] [4, 5] = min_heap, but due to implementation
# using heapq library we have [-3, -1]
# We decide to have more numbers in the max heap
class MedianOfAStream:
    max_heap = []
    min_heap = []

    # Time complexity of insert will be O(logn), due to insertion in a heap,
    # Space complexity will be O(n) because at any time we will be storing all the numbers
    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    # Time complexity will be O(1)
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0

        return -self.max_heap[0] / 1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
