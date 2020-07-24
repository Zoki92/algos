"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Real Input:
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

1. For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6−1)/5=>2.2(1+3+2+6-1)/5 => 2.2(1+3+2+6−1)/5=>2.2
2. The average of next 5 numbers (subarray from index 1-5) is: (3+2+6−1+4)/5=>2.8(3+2+6-1+4)/5 => 2.8(3+2+6−1+4)/5=>2.8
3. For the next 5 numbers (subarray from index 2-6), the average is: (2+6−1+4+1)/5=>2.4(2+6-1+4+1)/5 => 2.4(2+6−1+4+1)/5=>2.4

A brute-force algorithm will be to calculate the sum of every 5-element contiguous subarray of the given array and divide the 
sum by ‘5’ to find the average. This is what the algorithm will look like:
"""
import pytest
from typing import List


def find_averages_of_subarrays(array: List[int], k: int) -> List[float]:
    result = []
    for i in range(len(array) - k + 1):
        # find sum of the next k elements
        _sum = 0
        for j in range(i, i + k):
            _sum += array[j]
        result.append(_sum / k)
    return result


test_data = [
    ([1, 3, 2, 6, -1, 4, 1, 8, 2], 5, [2.2, 2.8, 2.4, 3.6, 2.8]),
]


@pytest.mark.parametrize("input_array, k, expected", test_data)
def test_find_averages_of_subarrays(
    input_array: List[int], k: int, expected: List[float],
):
    # for item in expected:
    assert find_averages_of_subarrays(input_array, k) == expected


"""Since for every element of the array we are calculating the sum of the next K elements
the time complexity of this algorithm will be O(N*K) where N is the number of elements in the input array
The inneficieny is that for any two consecutive subarrays of size 5, the overlapping part (which contains 4 elements)
will be evaluated twice
"""

# Time complexity O(n)
def find_averages_of_subarrays_frame(array: List[int], k: int) -> List[float]:
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(array)):
        window_sum += array[window_end]
        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= array[window_start]
            window_start += 1
    return result


@pytest.mark.parametrize("input_array, k, expected", test_data)
def test_find_averages_of_subarrays_frame(
    input_array: List[int], k: int, expected: List[float],
):
    # for item in expected:
    assert find_averages_of_subarrays_frame(input_array, k) == expected
