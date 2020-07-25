"""Given a string, find the length of the longest substring in it with no more than K distinct characters.
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

import pytest
from typing import List

# The time complexity of the above algorithm will be O(N)
# The outer for loop runs for all characters and the inner while loop processes each
# character only once, therefore the time complexity of the algorithm will be O(N+N)
# which is asymptotically equivalent to O(N)
# The space complexity of the algorithm is O(K) where k is distinct chars in the string
def longest_substring_with_k_distinct(test_str: str, k: int) -> int:
    longest = 0
    window_start = 0
    char_frequence = {}
    for window_end in range(len(test_str)):
        right_char = test_str[window_end]
        if right_char not in char_frequence:
            char_frequence[right_char] = 0
        char_frequence[right_char] += 1

        while len(char_frequence) > k:
            left_char = test_str[window_start]
            char_frequence[left_char] -= 1
            if char_frequence[left_char] == 0:
                del char_frequence[left_char]
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    return longest


test_data = [
    ("araaci", 2, 4),
    ("araaci", 1, 2),
    ("cbbebi", 3, 5),
]


@pytest.mark.parametrize("input_string, k, expected", test_data)
def test_longest_substring_with_k_distinct(
    input_string: str, k: int, expected: int,
):
    # for item in expected:
    assert longest_substring_with_k_distinct(input_string, k) == expected

