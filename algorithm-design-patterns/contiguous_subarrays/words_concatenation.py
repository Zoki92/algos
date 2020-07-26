"""Given a string and a list of words, find all the starting indices of substrings in 
the given string that are a concatenation of all the given words exactly once without 
any overlapping of words. It is given that all words are of the same length.

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""
import pytest
from typing import List

"""
Keep the frequency of every word in a HashMap.
Starting from every index in the string, try to match all the words.
In each iteration, keep track of all the words that we have already seen in another HashMap.
If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
Store the index if we have found all the words.
"""
# TODO get back to this and try again

# The time complexity of the above algorithm will be O(N∗M∗Len) where ‘N’
# is the number of characters in the given string, ‘M’ is the total number of words,
# and ‘Len’ is the length of a word.
# The space complexity of the algorithm is O(M) since at most, we will be storing all
# the words in the two HashMaps. In the worst case, we also need O(N) space for the resulting list.
# So, the overall space complexity of the algorithm will be O(M+N).
def find_word_concatenation(input_s: str, words: List[str]) -> List[int]:
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(input_s) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # get the next word from the string
            word = input_s[next_word_index : next_word_index + word_length]
            if word not in word_frequency:
                break

            # add the word to the words seen map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # no need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:
                result_indices.append(i)
    return result_indices


test_data = [
    ("catfoxcat", ["cat", "fox"], [0, 3]),
    ("catcatfoxfox", ["cat", "fox"], [3]),
]


@pytest.mark.parametrize("input_str, words, expected", test_data)
def test_find_word_concatenation(
    input_str: str, words: List[str], expected: List[int],
):
    # for item in expected:
    assert find_word_concatenation(input_str, words) == expected
