"""
Given a string and a number ‘K’, find if the string can be rearranged 
such that the same characters are at least ‘K’ distance apart from each other.

Example 1:

Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.

Example 2:

Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
Explanation: All same characters are 3 distance apart.

Example 3:

Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.

Example 4:

Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
"""
import pytest
from typing import List
from heapq import *
from collections import deque

# The time complexity of the above algorithm is O(N*logN) where ‘N’ is
# the number of characters in the input string.
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
def reorganize_string(str, k):
    if k <= 1:
        return str
    char_frequencies = {}
    for char in str:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1
    max_heap = []
    # add all chars in max heap
    for char, freq in char_frequencies.items():
        heappush(max_heap, (-freq, char))

    queue = deque()
    result_string = []
    while max_heap:
        freq, char = heappop(max_heap)
        # append the current character to the result string and decrement its count
        result_string.append(char)
        # decrement the frequency and append to the queue
        queue.append((char, freq + 1))
        if len(queue) == k:
            char, freq = queue.popleft()
            if -freq > 0:
                heappush(max_heap, (freq, char))
    # if we were successful in appending all the characters to the result string return it
    return "".join(result_string) if len(result_string) == len(str) else ""


test_data = [
    ("mmpp", 2, ["mpmp", "pmpm"]),
    ("Programming", 3, ["rgmPrgmiano", "gmringmrPoa", "gmrPagimnor"]),
    ("aab", 2, "aba"),
    ("aappa", 3, ""),
]


@pytest.mark.parametrize("str, k, expected", test_data)
def test_reorganize_string(str, k, expected):
    if isinstance(expected, List):
        assert reorganize_string(str, k) in expected
    else:
        assert reorganize_string(str, k) == expected

