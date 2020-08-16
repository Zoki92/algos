"""
Given an array nums of n integers where n > 1,  return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]


Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array 
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for 
the purpose of space complexity analysis.)



current index is 0

window will be current_index + 1 + len(arr) - 2, 
thats
 1 + 4 - 2 = 3
 1, 2, 3, indexes


current index is 1
window will be 

2 3 4, 4 > len(arr) - 1 so we need to do , 4 % len(4) == 0
2 3 0 indexes

current index is 2
window will be

3 4 5, or 3, 4 % 4 = 0, 5 % 4 = 1, thats 3, 0, 1

"""
import pytest
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    output = [1]
    for i in range(1, len(nums)):
        output.append(output[-1] * nums[i - 1])
    current_product = 1
    for i in range(len(nums) - 2, -1, -1):
        current_product *= nums[i + 1]
        output[i] *= current_product
    return output


test_data = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected
