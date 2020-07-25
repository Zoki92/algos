"""Given a string and pattern find out if the string contains any permutations of the pattern
Permutation is defined as rearranging the characters of the string. For example abc has these permutations:
abc
acb
bac
bca
cab
cba

if a string has n distinct characters it will have n! permutations

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""
import pytest


def find_permutation(input_str: str, pattern: str) -> bool:
    window_size = len(pattern)
    window_start = 0
    for window_end in range(len(input_str)):
        if window_end + window_size - 1 <= len(input_str) - 1:
            if is_permutation(
                pattern, input_str[window_start : window_end + window_size]
            ):
                return True
        window_start += 1
    return False


def is_permutation(pattern: str, possible_perm: str) -> bool:
    if sorted(pattern) == sorted(possible_perm):
        return True
    return False


test_data = [
    ("oidbcaf", "abc", True),
    ("odicf", "dc", False),
    ("bcdxabcdy", "bcdyabcdx", True),
]


@pytest.mark.parametrize("input_str, pattern, expected", test_data)
def test_find_permutation(
    input_str: str, pattern: str, expected: bool,
):
    # for item in expected:
    assert find_permutation(input_str, pattern) == expected


"""Better solution:
 - Create hash map that holds the frequencies of chars in the pattern
 - Iterate through the string adding one character at a time in the sliding window
 - If the character being added matches a char in the frequencies decrement it's frequency 
 - If the character frequency becomes zero we got a complete match
 - If at any time the number of chars matched is equal to the number of distinct chars in the pattern
we have gotten our complete permutation.
 - If the window size is greater than the length of the pattern shrink the window to make it equal to the size
 of the pattern. At the same time, if the character going out was part of the pattern put it back in the frequency
 of the hash map.
"""


def find_permutation_2(input_str: str, pattern: str) -> bool:
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the char frequency with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(input_str)):
        right_char = input_str[window_end]

        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            matched += 1
        if matched == len(pattern):
            return True
        if window_end >= len(pattern) - 1:
            left_char = input_str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                    char_frequency[left_char] += 1

    return False


@pytest.mark.parametrize("input_str, pattern, expected", test_data)
def test_find_permutation_2(
    input_str: str, pattern: str, expected: bool,
):
    # for item in expected:
    assert find_permutation_2(input_str, pattern) == expected
