""" Write an algorithm that implements selection sort
It works:
It finds the minimum element and places it in position 0 for first iteration
then 1 for second and so on.
"""
from timer_decorator import timer 


@timer
def selection_sort(array):
    current_idx = 0
    while current_idx < len(array) - 1:
        min_idx = current_idx
        for j in range(current_idx + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[current_idx], array[min_idx] = array[min_idx], array[current_idx]
        current_idx += 1
    return array
    

@timer
def selectionSort(array):
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[i] < array[smallest_idx]:
                smallest_idx = i
        swap(current_idx, smallest_idx, array)
        current_idx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
        
                
            
array = [8, 5, 2, 9, 5, 6, 3]

print(selection_sort(array))
selectionSort(array)