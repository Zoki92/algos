"""Write insertion sort algorithm
How it works:
8 5 2 9 5 6 3
5 8 2 9 5 6 3
2 5 8 9 5 6 3
2 5 5 8 9 6 3
2 5 5 6 8 9 3
2 3 5 5 6 8 9
"""

from timer_decorator import timer


@timer
def insertion_sort(array):

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] < array[j]:
                insert(i, j, array)

    return array

def insert(current_idx, insert_at, array):
    array.insert(insert_at, array[current_idx])
    array.pop(current_idx + 1)


@timer
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j - 1, j, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]




array = [8, 5, 2, 9, 5, 6, 3]

print(insertionSort(array))