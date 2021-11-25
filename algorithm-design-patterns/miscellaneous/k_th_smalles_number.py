from typing import List
import pytest


def find_kth_smallest_number(nums: List[int], k: int) -> int:
    """
    Given an unsorted array of numbers, find the Kth smallest number in it.
    Input: [1, 5, 12, 2, 11, 5], K = 3
    Output: 5
    Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

    Solution can use the Median of Medians algorithm to choose a good pivot for the partitioning algorithm of the
    quicksort. This algorithm finds an approximate median of an array in linear time O(N). When this approximate
    median is used as the pivot, the worst case complexity of the partitioning procedure reduces to linear O(N),
    which is also the asymptotically optimal worst-case complexity of any sorting/selection algorithm.
    1. If we have 5 or less than 5 elements in the input array we simply take its first element as the pivot. If not
    then we divide the input array into subarrays of five elements (for simplicity can ingore any subarray with less than 5 elements)
    2. Sort each subarray to determine it's median. Sorting a small and fixed numbered array takes constant time. At the end
    of this step, we have an array containing medians of all the subarray.
    3. Recursively call the partitioning algorithm on the array containing medians until we get our pivot.
    4. Everytime the partition procedure needs to find a pivot it will follow the above three steps.
    """
    return recursion_helper(nums, k, 0, len(nums) - 1)


def recursion_helper(nums, k, start, end):
    p = partition(nums, start, end)
    if p == k - 1:
        return nums[p]

    if p > k - 1:
        return recursion_helper(nums, k, start, p - 1)

    return recursion_helper(nums, k, p + 1, end)


def partition(nums, low, high):
    if low == high:
        return low
    median = median_of_medians(nums, low, high)
    # find the median in the array and swap it with nums[high] which will become our pivot
    for i in range(low, high):
        if nums[i] == median:
            nums[i], nums[high] = nums[high], nums[i]
            break

    pivot = nums[high]
    for i in range(low, high):
        # all elements less than the pivot will be before index low
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1

    # put the pivot in its correct place
    nums[low], nums[high] = nums[high], nums[low]
    return low


def median_of_medians(nums, low, high):
    n = high - low + 1
    # if we have less than 5 elements ingore the partitioning algorithm
    if n < 5:
        return nums[low]

    # partition the given array into chunks of 5 elements
    partitions = [nums[j : j + 5] for j in range(low, high + 1, 5)]

    # for simplicity ignore partition with less than 5 elements
    full_partitions = [partition for partition in partitions if len(partition) == 5]

    # sort all partitions
    sorted_partitions = [sorted(partition) for partition in full_partitions]

    # find median of all partitions; the median is at position 2
    medians = [partition[2] for partition in sorted_partitions]

    return partition(medians, 0, len(medians) - 1)


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    (
        ([1, 5, 12, 2, 11, 5], 3, 5),
        ([1, 5, 12, 2, 11, 5], 4, 5),
        ([5, 12, 11, -1, 12], 3, 11),
    ),
)
def test_find_kth_smallest_number(nums: List[int], k: int, expected: int) -> None:
    assert find_kth_smallest_number(nums, k) == expected
