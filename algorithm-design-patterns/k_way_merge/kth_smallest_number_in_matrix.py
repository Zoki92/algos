"""
Given an N * N matrix where each row and column is sorted in ascending order, 
find the Kth smallest element in the matrix.

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
"""
import pytest
from typing import List
from heapq import *
import pytest

# First, we inserted at most ‘K’ or one element from each of the ‘N’ rows, which will take O(min(K, N)).
# Then we went through at most ‘K’ elements in the matrix and remove/add one element in the heap in each step.
# As we can’t have more than ‘N’ elements in the heap in any condition, therefore, the overall time complexity
# of the above algorithm will be O(min(K, N) + K*logN).
# The space complexity will be O(N) because, in the worst case, our min-heap will be storing one number from
#  each of the ‘N’ rows.
def find_Kth_smallest(matrix: List[List[int]], k: int) -> int:
    min_heap = []

    # put the first element of each row in the min heap
    # we don't need to push more than k elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    # take the smallest top element from the min heap, if the running count is equal to k return the number
    # if the row of the top element has more elements, add the next element of the heap
    number_count, number = 0, 0
    while min_heap:
        number, i, row = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break
        if len(row) > i + 1:
            heappush(min_heap, (row[i + 1], i + 1, row))

    return number


test_data = [
    ([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5, 7),
]


@pytest.mark.parametrize("matrix, k, expected", test_data)
def test_find_Kth_smallest(matrix, k, expected):
    assert find_Kth_smallest(matrix, k) == expected


# alternative
# The Binary Search could take O(log(max-min )) iterations where ‘max’
# is the largest and ‘min’ is the smallest element in the matrix and in each iteration we take O(N)
# for counting, therefore, the overall time complexity of the algorithm will be O(N*log(max-min)).
# The algorithm runs in constant space O(1).
def find_Kth_smallest(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger

