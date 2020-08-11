"""
Given an expression containing digits and operations (+, -, *), find all possible ways in which
the expression can be evaluated by grouping the numbers and operators using parentheses.


Input: "1+2*3"
Output: 7, 9
Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

Input: "2*3-4-5"
Output: 8, -12, 7, -7, -3 
Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3


"""
import pytest
from typing import List

"""
The time complexity of this algorithm will be exponential and will be similar to Balanced Parentheses.
Estimated time complexity will be O(N*2^N) but the actual time complexity O(4^n/sqrt{n})
is bounded by the Catalan number and is beyond the scope of a coding interview.

The space complexity of this algorithm will also be exponential, estimated at  O(N*2^N) 
though the actual will be O(4^n/sqrt{n}).
"""


def diff_ways_to_evaluate_expression(input: str) -> List[str]:
    result = []
    if "+" not in input and "-" not in input and "*" not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            char = input[i]
            if not char.isdigit():
                left_parts = diff_ways_to_evaluate_expression(input[0:i])
                right_parts = diff_ways_to_evaluate_expression(input[i + 1 :])
                for part1 in left_parts:
                    for part2 in right_parts:
                        if char == "+":
                            result.append(part1 + part2)
                        elif char == "-":
                            result.append(part1 - part2)
                        elif char == "*":
                            result.append(part1 * part2)

    return result


"""
The problem has overlapping subproblems, as our recursive calls can be evaluating the same sub-expression multiple times. 
To resolve this, we can use memoization and store the intermediate results in a HashMap. 
In each function call, we can check our map to see if we have already evaluated this sub-expression before. 
Here is the memoized version of our algorithm:
"""


def diff_ways_to_evaluate_expression_memoized(input: str) -> List[int]:
    return diff_ways_to_evaluate_expression_rec({}, input)


def diff_ways_to_evaluate_expression_rec(map, input):
    if input in map:
        return map[input]

    result = []

    if "+" not in input and "-" not in input and "*" not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            char = input[i]
            if not char.isdigit():
                left_parts = diff_ways_to_evaluate_expression_rec(map, input[0:i])
                right_parts = diff_ways_to_evaluate_expression_rec(map, input[i + 1 :])

                for part1 in left_parts:
                    for part2 in right_parts:
                        if char == "+":
                            result.append(part1 + part2)
                        elif char == "-":
                            result.append(part1 - part2)
                        elif char == "*":
                            result.append(part1 * part2)
    map[input] = result
    return result


test_data = [("1+2*3", [7, 9]), ("2*3-4-5", [8, -12, 7, -7, -3])]


@pytest.mark.parametrize("input_, expected", test_data)
def test_diff_ways_to_evaluate_expression(input_: str, expected: List[str]):
    assert diff_ways_to_evaluate_expression(input_) == expected


@pytest.mark.parametrize("input_, expected", test_data)
def test_diff_ways_to_evaluate_expression_memoized(input_: str, expected: List[str]):
    assert diff_ways_to_evaluate_expression_memoized(input_) == expected
