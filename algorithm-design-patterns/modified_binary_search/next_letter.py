"""
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter.
 This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first 
 letter of the array.

Write a function to return the next letter of the given ‘key’.

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""
import pytest
from typing import List

# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def search_next_letter(letters: List[str], key: str) -> str:
    n = len(letters)
    if key < letters[0] or key > letters[n - 1]:
        return letters[0]

    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % n]


test_data = [
    (["a", "c", "f", "h"], "f", "h"),
    (["a", "c", "f", "h"], "b", "c"),
    (["a", "c", "f", "h"], "m", "a"),
    (["a", "c", "f", "h"], "h", "a"),
]


@pytest.mark.parametrize("letters, key, expected", test_data)
def test_search_next_letter(letters: List[str], key: str, expected: str):
    assert search_next_letter(letters, key) == expected
