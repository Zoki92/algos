"""Write a function that takes in a sorted array of distinct integers as well as a target integer.
The integers in the array have been shifted by some amount;
"""

def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array)-1)

def shiftedBinarySearchHelper(array, target, left, right):

    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        left_num = array[left]
        right_num = array[right]
        if target == potential_match:
            return middle
        elif left_num <= potential_match:
            if target < potential_match and target >= left_num:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target > potential_match and target <= right_num:
                left = middle + 1
            else:
                right = middle - 1
    return -1