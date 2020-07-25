"""Given a string, find the length of the longest substring which has no repeating characters.
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
"""
import pytest


def non_repeat_substring(input_s: str) -> int:
    window_start = 0
    unique_chars = {}
    max_substring = 0
    for window_end in range(len(input_s)):
        current_char = input_s[window_end]
        while current_char in unique_chars:
            max_substring = max(max_substring, len(unique_chars))
            del unique_chars[input_s[window_start]]
            window_start += 1
        unique_chars[current_char] = 0
    return max_substring


test_data = [
    ("aabccbb", 3),
    ("abbbb", 2),
    ("abccde", 3),
]


@pytest.mark.parametrize("input_s, expected", test_data)
def test_non_repeat_substring(
    input_s: str, expected: int,
):
    # for item in expected:
    assert non_repeat_substring(input_s) == expected


"""
We can use a hash map to remember the last index of each character we have processed. Whenever we get a repeating character
we will shrink our sliding window to ensure that we only have distinct characters in the sliding window
"""

# The time complexity of the above algorithm will be O(N)
# The space complexity will be O(K) where K is the length of the longest unique chars substring
# However since we only have 26 letters in the English letter and we only expect set of chars we
# can say that the algorithm runs in fixed O(1), which means that we can use fixed size array instead
# of hash map
def non_repeat_substring_2(input_s: str) -> int:
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(input_s)):
        right_char = input_s[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


@pytest.mark.parametrize("input_s, expected", test_data)
def test_non_repeat_substring_2(
    input_s: str, expected: int,
):
    # for item in expected:
    assert non_repeat_substring_2(input_s) == expected
