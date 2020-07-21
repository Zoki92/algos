"""Implement bubble sort algorithm in python"""
import timeit
import datetime

def bubble_sort(array):

    while True:
        swap_count_inner = 0
        print(array)
        for i in range(0, len(array)):
            
            if i < len(array) - 1 and array[i] > array[i+1]:
                swap(i, i + 1, array)
                swap_count_inner += 1
        
        if swap_count_inner == 0:
            break
    return array


""" from understanding,
Best time is O(n), 
Average O(n^2),
Worst O (n^2)
"""
from timer_decorator import timer


@timer
def bubbleSort2(array):
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
        counter += 1
    return array

        
    
def swap(first, second, array):
    array[first], array[second] = array[second], array[first]

array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort2(array))

# times = []
# for i in range(100):
#     start = datetime.datetime.now()
#     bubleSort(array)
#     end = datetime.datetime.now()
#     times.append((end - start).microseconds)

# times_mine = []
# for i in range(100):
#     start = datetime.datetime.now()
#     bubble_sort(array)
#     end = datetime.datetime.now()
#     times_mine.append((end - start).microseconds)

# import functools
# print("clems average: ", functools.reduce(lambda a, b: a + b, times) / 100)
# print("mine average: ", functools.reduce(lambda a, b: a + b, times_mine) / 100)
