"""Implement merge sort in Python"""
from timer_decorator import timer

# O(nlogn) time and O(nlogn) space
def merge_sort(array):
    if len(array) == 1:
        return array
    middle_idx = len(array) // 2
    left_half = array[:middle_idx]
    right_half = array[middle_idx:]
    return merge_sorted_arrays(merge_sort(left_half), merge_sort(right_half))

def merge_sorted_arrays(left_half, right_half):

    sorted_array = [None] * (len(left_half) + len(right_half))
    
    k = i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1

    return sorted_array





@timer    
def mergeSort(array):
    if len(array) == 1:
        return array
    helper = array[:]
    mergeSortHelper(array, 0, len(array) - 1, helper)
    return array

def mergeSortHelper(array, start_idx, end_idx, helper):
    if start_idx == end_idx:
        return
    middle_idx = (start_idx + end_idx) // 2
    mergeSortHelper(helper, start_idx, middle_idx, array)
    mergeSortHelper(helper, middle_idx + 1, end_idx, array)

    mergeArrays(array, start_idx, middle_idx, end_idx, helper)

def mergeArrays(array, start_idx, middle_idx, end_idx, helper):
    k = start_idx
    i = start_idx
    j = middle_idx + 1

    while i <= middle_idx and j <= end_idx:
        if helper[i] <= helper[j]:
            array[k] = helper[i]
            i += 1
        else:
            array[k] = helper[j]
            j += 1
        k += 1
    while i <= middle_idx:
        array[k] = helper[i]
        i += 1
        k += 1
    while j <= end_idx:
        array[k] = helper[j]
        j += 1
        k += 1
        
    
@timer 
def mergeSortt(arr):
    mergeSorttHelper(arr)
    return arr


def mergeSorttHelper(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSorttHelper(L) # Sorting the first half 
        mergeSorttHelper(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
    return arr

array = [8, 5, 2, 9, 5, 6, 3]

print(mergeSort(array))
print(mergeSortt(array))
