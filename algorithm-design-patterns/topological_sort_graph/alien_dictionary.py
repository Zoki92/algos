from collections import deque
from typing import List

import pytest


def find_order(words: List[str]) -> str:
    """
    There is a dictionary containing words from an alien language for which we don’t know the
    ordering of the alphabets. Write a method to find the correct order of the alphabets in the
    alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.

    Input: Words: ["ba", "bc", "ac", "cab"]
    Output: bac
    Explanation: Given that the words are sorted lexicographically by the rules of the alien     language, so
    from the given words we can conclude the following ordering among its characters:

    1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
    2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

    From the above two points, we can conclude that the correct character order is: "bac"

    Since the given words are sorted lexicographically by the rules of the alien language, we can
    always compare two adjacent words to determine the ordering of the characters. Take Example-1 above: [“ba”, “bc”, “ac”, “cab”]

    Take the first two words “ba” and “bc”. Starting from the beginning of the words, find the first character
    that is different in both words: it would be ‘a’ from “ba” and ‘c’ from “bc”. Because of the sorted order
    of words (i.e. the dictionary!), we can conclude that ‘a’ comes before ‘c’ in the alien language.
    Similarly, from “bc” and “ac”, we can conclude that ‘b’ comes before ‘a’.
    These two points tell us that we are actually asked to find the topological ordering of the characters,
    and that the ordering rules should be inferred from adjacent words from the alien dictionary.

    This makes the current problem similar to Tasks Scheduling Order, the only difference being that we need
    to build the graph of the characters by comparing adjacent words first, and then perform the topological
    sort for the graph to determine the order of the characters.

    Time complexity #
    In step ‘d’, each task can become a source only once and each edge (a rule) will be accessed and removed once.
    Therefore, the time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of
    different characters and ‘E’ is the total number of the rules in the alien language. Since, at most, each pair
    of words can give us one rule, therefore, we can conclude that the upper bound for the rules is O(N)
    where ‘N’ is the number of words in the input. So, we can say that the time complexity of our algorithm is O(V+N).

    Space complexity #
    The space complexity will be O(V+N), since we are storing all of the rules for each character in an adjacency list.
    """
    order = None
    if len(words) == 0:
        return ""

    in_degree = {}
    graph = {}

    # initialize the graph
    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []

    # build the graph
    for i in range(0, len(words) - 1):
        # find ordering of characters from adjacent words
        w1, w2 = words[i], words[i + 1]
        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            # if the two characters are different
            if parent != child:
                # put the child in it's parent's list
                graph[parent].append(child)
                in_degree[child] += 1
                # only the first different character between the two words will help us find the order
                break

    sources = deque()

    for key, value in in_degree.items():
        if value == 0:
            sources.append(key)

    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    if len(sorted_order) != len(in_degree):
        return ""
    order = "".join(sorted_order)
    return order


@pytest.mark.parametrize(
    ("words, expected"),
    (
        (["ba", "bc", "ac", "cab"], "bac"),
        (["cab", "aaa", "aab"], "cab"),
        (["ywx", "wz", "xww", "xz", "zyy", "zwz"], "ywxz"),
    ),
)
def test_find_order(words: List[str], expected: str):
    assert find_order(words) == expected
