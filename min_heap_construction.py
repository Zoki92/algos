"""Min heap construction.
 - Min heap in the form of an array
 - Min heap means that the value of the parent has to be less than or equal
 than the children nodes values and the value of the root has to be the smallest
 value in the heap
"""


class MinHeap:
    def __init__(self, input_array):
        self.heap = self.build_min_heap(input_array)
    
    # O(n) time O(1) space
    def build_min_heap(self, input_array):
        """finds the first parent index, and then sifts it down
        and goes to all the parents and does the same
        """
        first_parent_idx = (len(input_array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(input_array) -1, input_array)
        return input_array
    
    # O(logn) time O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)
    
    # O(logn) time O(1) space
    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2
    
    # O(logn) time O(1) space
    def remove(self):
        self.swap(0, self.heap_length-1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, self.heap_length-1, self.heap)
        return value_to_remove
    
    # O(logn) time O(1) space
    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_one_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return
    
    def peek(self):
        return self.heap[0]

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    @property
    def heap_length(self):
        return len(self.heap)

test_array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

min_heap = MinHeap(test_array)

print(min_heap.heap)