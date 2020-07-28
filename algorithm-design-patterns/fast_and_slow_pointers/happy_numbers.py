"""
Any number will be called a happy number if, after repeatedly replacing it with a number
equal to the sum of the square of all of its digits, leads us to number ‘1’. All other 
(not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
2​^2​​ + 3^​2​​ = 4 + 9 = 13
1^2 + 3^2​​ = 1 + 9 = 10
1^2 + 0^2​​ = 1 + 0 = 1


Input: 12   
Output: false (12 is not a happy number)  
"""
import pytest

"""
The process, defined above, to find out if a number is a happy number or not, always ends in a cycle. 
If the number is a happy number, the process will be stuck in a cycle on number ‘1,’ and if the number 
is not a happy number then the process will be stuck in a cycle with a set of numbers. As we saw in Example-2
 while determining if ‘12’ is a happy number or not, our process will get stuck in a cycle with the following 
 numbers: 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

We saw in the LinkedList Cycle problem that we can use the Fast & Slow pointers method to find a cycle among 
a set of elements. As we have described above, each number will definitely have a cycle. Therefore, we will 
use the same fast & slow pointer strategy to find the cycle and once the cycle is found, we will see if the 
cycle is stuck on number ‘1’ to find out if the number is happy or not.
"""


def find_happy_number(num: int) -> bool:
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:
            break
    return slow == 1  # see if the cycle is stuck on the number 1


def find_square_sum(num: int) -> int:
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


test_data = [
    (23, True),
    (12, False),
]


@pytest.mark.parametrize("num, expected", test_data)
def test_find_happy_number(
    num: int, expected: int,
):
    # for item in expected:
    assert find_happy_number(num) == expected
