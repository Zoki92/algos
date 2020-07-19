"""Binary search algorithm"""

def binary_search(array, target):
    
    mid = len(array) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        if len(array) == 1:
            return False
        return binary_search(array[:mid], target)
    else:
        if len(array) == 1:
            return False
        return binary_search(array[mid:], target)
    return False



# O(logn) time O(logn) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if potential_match == target:
        return middle
    elif target < potential_match:
        return binarySearchHelper(array, target, left, middle -1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)




def binary_search_with_index(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        potential = array[mid]
        if potential == target:
            return mid
        elif potential > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

target = 21

print(binary_search_with_index(array, 73))