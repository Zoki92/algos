"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""
import pytest
from typing import List


# Since we can have 2^N​​ permutations at the most and while processing each
# permutation we convert it into a character array, the overall time complexity of the algorithm will be O(N∗2^N).
# All the additional space used by our algorithm is for the output list. Since we can have a total of
# 2^N​​ permutations, the space complexity of our algorithm is O(N∗2^N).
def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append("".join(chs))

    return permutations


test_data = [
    ("ad52", ["ad52", "Ad52", "aD52", "AD52"]),
    ("ab7c", ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]),
]


@pytest.mark.parametrize("str, expected", test_data)
def test_find_letter_case_string_permutations(str, expected):
    assert find_letter_case_string_permutations(str) == expected
