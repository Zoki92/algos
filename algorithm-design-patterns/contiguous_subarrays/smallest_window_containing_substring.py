"""Given a string and a pattern, find the smallest substring in the given string which 
has all the characters of the given pattern.

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

"""

import pytest
import math


"""
- Will keep a running track of every matching instance of a character.
- Whenever we have matched all the characters we will try to shrink the window from the beginning,
keeping track of the smallest substring that has all the matching characters.
- We will stop the shrinking process as soon as we remove a matched character from the sliding window.
One thing to note here is that we could have redundant matching characters. In this case when we encounter
the first one then we will simply shrink the window without decrementing the matched count. We will decrement
the matched count when the second char goes out of the window.
"""

# The time complexity of the above algorithm will be O(N+M)
# where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.
# The space complexity of the algorithm is O(M)
# In the worst case, we also need O(N)space for the resulting substring
def find_substring(input_s: str, pattern: str):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(input_s) + 1
    char_frequency = {}

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

        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
            left_char = input_s[window_start]
            window_start += 1

            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(input_s):
        return ""
    return input_s[substr_start : substr_start + min_length]


test_data = [
    ("aabdec", "abc", "abdec"),
    ("abdabca", "abc", "abc"),
    ("adcad", "abc", ""),
]


@pytest.mark.parametrize("input_str, pattern, expected", test_data)
def test_find_substring(
    input_str: str, pattern: str, expected: str,
):
    # for item in expected:
    assert find_substring(input_str, pattern) == expected
