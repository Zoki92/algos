"""Given a string with lowercase letters only if you are allowed to replace no more than k letters with 
any letter find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
"""

import pytest

# The time complexity of the above algorithm will be O(N)
# Space complexity is O(1) because we can have maximum of 26 chars inside the hash map
# letters of the alphabet = 26
def length_of_longest_substring(input_s: str, k: int) -> int:
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for window_end in range(len(input_s)):
        right_char = input_s[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1

        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char]
        )

        # current window size is from window_start to window_end, overall we have  a letter which is
        # repeating 'max_repeat_letter_count' times, this means that we have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letter we should replace. If the remaining
        # letters are more than k it is time to shrink the window
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = input_s[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


test_data = [
    ("aabccbb", 2, 5),
    ("abbcb", 1, 4),
    ("abccde", 1, 3),
]


@pytest.mark.parametrize("input_s, k, expected", test_data)
def test_length_of_longest_substring(
    input_s: str, k: int, expected: int,
):
    # for item in expected:
    assert length_of_longest_substring(input_s, k) == expected

