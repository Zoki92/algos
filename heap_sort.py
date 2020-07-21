"""Implement heap sort in python"""

# Worst O(nlogn) time and O(1) space
def heapSort(array):
    buildHeap(array)
    for end_idx in reversed(range(len(array))):
        swap(0, end_idx, array)
        sift_down(0, end_idx - 1, array)
    return array



def buildHeap(array):
    first_parent_idx = (len(array)- 2) // 2
    for current_idx in reversed(range(first_parent_idx + 1)):
        sift_down(current_idx, len(array) - 1, array)


def sift_down(current_idx, end_idx, heap):
    child_one_idx = 2*current_idx + 1
    while child_one_idx <= end_idx:
        child_two_idx = 2*current_idx + 2 if current_idx * 2 + 2 <= end_idx else -1
        if child_two_idx > -1 and heap[child_one_idx] < heap[child_two_idx]:
            idx_to_swap = child_two_idx
        else:
            idx_to_swap = child_one_idx
        
        if heap[idx_to_swap] > heap[current_idx]:
            swap(current_idx, idx_to_swap, heap)
            current_idx = idx_to_swap
            child_one_idx = current_idx * 2 + 1
        else:
            return





def heap_sort(array):
    build_heap(array)
    for i in reversed(range(1, len(array))):
        swap(0, i, array)
        sift_down2(0, i - 1, array)
    return array


def build_heap(array):
    first_parent_idx = (len(array) - 2) // 2
    for current_idx in reversed(range(first_parent_idx + 1)):
        sift_down2(current_idx, len(array) - 1, array)



def sift_down2(current_idx, end_idx, array):
    first_child_idx = current_idx * 2 + 1
    while first_child_idx <= end_idx:
        second_child_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
        if second_child_idx > -1 and array[second_child_idx] > array[first_child_idx]:
            idx_to_swap = second_child_idx
        else:
            idx_to_swap = first_child_idx
        if array[idx_to_swap] > array[current_idx]:
            swap(idx_to_swap, current_idx, array)
            current_idx = idx_to_swap
            first_child_idx = idx_to_swap * 2 + 1
        else:
            return

def swap(i, j, array):
    array[i],array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
print(heap_sort(array))