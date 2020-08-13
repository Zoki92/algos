"""
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.

Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.

Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
"""
from heapq import *
import pytest
from typing import List


# The time complexity of the above algorithm is O(N*logN) where ‘N’ is
# the number of characters in the input string.
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the
def rearrange_string(str):
    char_frequency_map = {}
    for char in str:
        char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

    max_heap = []
    for char, frequency in char_frequency_map.items():
        heappush(max_heap, (-frequency, char))

    previous_char, previous_freq = None, 0
    result_string = []
    while max_heap:
        frequency, char = heappop(max_heap)
        # add the previous entry back in the heap if its frequency is greater than zero
        if previous_char and -previous_freq > 0:
            heappush(max_heap, (previous_freq, previous_char))
        # append the current char to the result string and decrement its count
        result_string.append(char)
        previous_char = char
        previous_freq = frequency + 1  # decrement the freqency (it's negative)

    # if we were successful in appending all the characters to the result string return it
    return "".join(result_string) if len(result_string) == len(str) else ""


test_data = [
    ("aappp", "papap"),
    ("Programming", ["rgmrgmPiano", "gmringmrPoa", "gmrPagimnor"]),
    ("aapa", ""),
]


@pytest.mark.parametrize("str, expected", test_data)
def test_rearrange_string(str, expected):
    if isinstance(expected, List):
        assert rearrange_string(str) in expected
    else:
        assert rearrange_string(str) == expected
