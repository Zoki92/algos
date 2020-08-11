"""
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses

Input: N=2
Output: (()), ()()

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""
import pytest
from typing import List
from collections import deque


class ParenthesisString:
    def __init__(self, str, open_count, closed_count):
        self.str = str
        self.open_count = open_count
        self.closed_count = closed_count


def generate_valid_parentheses(num: int) -> List[str]:
    result = []
    queue = deque()
    queue.append(ParenthesisString("", 0, 0))
    while queue:
        ps = queue.popleft()
        if ps.open_count == num and ps.closed_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                queue.append(
                    ParenthesisString(ps.str + "(", ps.open_count + 1, ps.closed_count)
                )
            if ps.open_count > ps.closed_count:
                queue.append(
                    ParenthesisString(ps.str + ")", ps.open_count, ps.closed_count + 1)
                )
    return result


class MyClass:
    def __init__(self, str, open_count, close_count):
        self.str = str
        self.open_count = open_count
        self.close_count = close_count

    def __repr__(self):
        return f"{self.str}"


"""
Let’s try to estimate how many combinations we can have for ‘N’ pairs of balanced parentheses. 
If we don’t care for the ordering - that ) can only come after ( - then we have two options 
for every position, i.e., either put open parentheses or close parentheses. This means we 
can have a maximum of 2^N​​ combinations. Because of the ordering, the actual number will be less than 2^N​​.

If you see the visual representation of Example-2 closely you will realize that, in the worst case, it is equivalent to a binary tree,
where each node will have two children. This means that we will have 2^N​​ leaf nodes and 2^N-1 intermediate nodes. So the total number
of elements pushed to the queue will be 2^N​​ + 2^N-1, which is asymptotically equivalent to O(2^N). While processing each element,
we do need to concatenate the current string with ( or ). This operation will take O(N), so the overall time complexity 
of our algorithm will be O(N*2^N). This is not completely accurate but reasonable enough to be presented in the interview.

All the additional space used by our algorithm is for the output list. Since we can’t have more 
than O(2^N) combinations, the space complexity of our algorithm is O(N*2^N)
"""


def my_func(num):
    result = []
    queue = deque()
    queue.append(MyClass("", 0, 0))

    while queue:
        print("Queue: ", queue)
        ps: MyClass = queue.popleft()
        if ps.close_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                queue.append(MyClass(ps.str + "(", ps.open_count + 1, ps.close_count))
            if ps.open_count > ps.close_count:
                queue.append(MyClass(ps.str + ")", ps.open_count, ps.close_count + 1))
    return result


test_data = [
    (2, ["(())", "()()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
]


@pytest.mark.parametrize("num, expected", test_data)
def test_generate_valid_parentheses(num: int, expected: List[str]):
    assert generate_valid_parentheses(num) == expected
