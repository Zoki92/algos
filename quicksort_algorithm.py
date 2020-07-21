"""Implement quick sort algorithm in python
How it works:
get a pivot and do a left and right
sort items so that the left is smaller than the pivot and the right is larger than the pivot

"""
from timer_decorator import timer

@timer
def quicksort(array):
    quicksort_helper(array, 0, len(array)-1)
    return array

def quicksort_helper(array, low, high):
    if low < high:
        p1 = partition(array, low, high)
        quicksort_helper(array, low, p1-1)
        quicksort_helper(array, p1+1, high)

def partition(array, low, high):
    i = high + 1
    pivot = array[low]
    for j in range(low + 1, high):
        if array[j] > pivot:
            i = i - 1
            swap(i, j, array)
    swap(i-1, high, array)
    return i - 1


@timer
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx
    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(left_idx, right_idx, array)
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    
    swap(pivot_idx, right_idx, array)

    left_subarray_is_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)

    if left_subarray_is_smaller:
        quickSortHelper(array, start_idx, right_idx - 1)
        quickSortHelper(array, right_idx + 1, end_idx)
    else:
        quickSortHelper(array, right_idx + 1, end_idx)
        quickSortHelper(array, start_idx, right_idx - 1)
    

            
    
    
def swap(i,j,array):
    array[i], array[j] = array[j],array[i]


array = [8, 5, 2, 9, 5, 6, 3]

print(quicksort(array))
# quickSort(array)



