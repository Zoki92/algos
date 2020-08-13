"""
Given a string, sort it based on the decreasing frequency of its characters.

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""
import pytest
from heapq import *


def sort_character_by_frequency(str):
    char_frequency = {}
    for char in str:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    max_heap = []
    for char, freq in char_frequency.items():
        heappush(max_heap, (-freq, char))

    sorted_string = []
    while max_heap:
        freq, char = heappop(max_heap)
        for _ in range(-freq):
            sorted_string.append(char)

    return "".join(sorted_string)


test_data = [
    ("Programming", "rrggmmPiano"),
    ("abcbab", "bbbaac"),
]


@pytest.mark.parametrize("str, expected", test_data)
def test_sort_character_by_name(str, expected):
    assert sorted(sort_character_by_frequency(str)) == sorted(expected)

