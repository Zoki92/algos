"""Write a function that takes sorted array of integers and target. The function should use a variety of binary search algorithm
to find a range of indices between which the target number is container in the array and should return this range in the form 
of an array"""


def searchForRange(array, target):

    left = 0
    right = len(array) - 1
    indice = []
    while left <= right:

        mid = (left + right) // 2
        potential = array[mid]
        if potential == target:
            # we are inside indice
            start = mid
            end = mid

            while array[end] == target:
                if end == len(array) - 1:
                    end += 1
                    break
                end += 1
            while array[start] == target:
                if start == 0:
                    break
                start -= 1
            return [start+1, end-1]
        elif potential < target:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]


array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 10
array2 = [5, 7, 7, 8, 8, 10]

print(searchForRange(array2, target))


# This solution is O(logn) and O(1) space
def searchForRange(array, target):
    final_range = [-1, -1]
    altered_binary_search_right(array, target, 0, len(array) - 1, final_range)
    altered_binary_search_left(array, target, 0, len(array) - 1, final_range)
    return final_range
    
 
def altered_binary_search_right(array, target, left, right, final_range):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                final_range[1] = mid
                return
            else:
                left = mid + 1
    
    
def altered_binary_search_left(array, target, left, right, final_range):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or array[mid - 1] != target:
                final_range[0] = mid
                return
            else:
                right = mid - 1