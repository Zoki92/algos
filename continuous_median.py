"""Write a continuous median handler that supports:
- The continuous inseertion of numbers with the insert method
- The instant O(1) time retrieval of the median of the numbers
 that have been inserter thus far with the getMedian method
"""


class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = HEAP(MIN_HEAP_FUNC, [])
        self.median = None
    
    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalance_heaps()
        self.update_median()
    
    def rebalance_heaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())
    
    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()
    
    def getMedian(self):
        return self.median

def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b

class Heap:
    def __init__(self, comparison_func, array):
        self.comparison_func = comparison_func
        self.heap = self.build_heap(array)
        self.length = len(self.heap)
    
    def build_heap(self, array):
        first_parent_idx = (len(array)-2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(current_idx, len(array) - 1, array)
        return array
    
    def siftDown(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1:
                if self.comparison_func(heap[child_two_idx], heap[child_one_idx]):
                    idx_to_swap = child_two_idx
                else:
                    idx_to_swap = child_one_idx
            else:
                idx_to_swap = child_one_idx
            if self.comparison_func(heap[idx_to_swap], heap[current_idx]):
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return
    
    def siftUp(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0:
            if self.comparison_func(heap[current_idx], heap[parent_idx]):
                self.swap(current_idx, parent_idx, heap)
                current_idx = parent_idx
                parent_idx = (current_idx - 1) // 2
            else:
                return
    
    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, self.length -1, self.heap)
        value_to_remove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length -1, self.heap)
        return value_to_remove
    
    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length-1, self.heap)
    
    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

continuous_median = ContinuousMedian()

continuous_median.insert(5)
continuous_median.insert(10)
print(continuous_median.getMedian())
continuous_median.insert(100)
print(continuous_median.getMedian())
