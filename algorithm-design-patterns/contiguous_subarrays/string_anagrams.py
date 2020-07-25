"""Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

    abc
    acb
    bac
    bca
    cab
    cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""
import pytest
from typing import List


# The time complexity of the above algorithm will be O(N+M)
# where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.
# The space complexity of the algorithm is O(M)O(M)O(M) since in the worst case, the whole pattern
# can have distinct characters which will go into the HashMap. In the worst case, we also need O(N)
# space for the result list, this will happen when the pattern has only one character and the string
# contains only that character.
def find_string_anagrams(input_s: str, pattern: str) -> List[int]:
    window_start, matched = 0, 0
    start_index = 0
    char_frequency = {}
    start_indices = []

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(input_s)):
        right_char = input_s[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1

        if matched == len(pattern):
            start_indices.append(window_end - len(pattern) + 1)

        if window_end >= len(pattern) - 1:
            left_char = input_s[window_start]
            window_start += 1

            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                    char_frequency[left_char] += 1
    return start_indices


test_data = [
    ("ppqp", "pq", [1, 2]),
    ("abbcabc", "abc", [2, 3, 4]),
]


@pytest.mark.parametrize("input_str, pattern, expected", test_data)
def test_find_string_anagrams(
    input_str: str, pattern: str, expected: List[int],
):
    # for item in expected:
    assert find_string_anagrams(input_str, pattern) == expected


find_string_anagrams(
    "ppqp", "pq",
)

