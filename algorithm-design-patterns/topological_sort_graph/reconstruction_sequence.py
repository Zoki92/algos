from collections import deque
from typing import List

import pytest


def can_construct(original_seq: List[int], sequences: List[List[int]]) -> bool:
    """
    Given a sequence and an array of sequences, write a method to find if this sequence can be uniquely
    reconstructed from the array of sequences, this means that original sequence is the only sequence such
    that all sequences in the array are subsequences of it.

    Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
    Output: true
    Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct
    [1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers
    in the 'originalSeq'.

    Solutin:
    Since each sequence in the given array defines the ordering of some numbers, we need to combine all these ordering rules to find
    two things:
    - Is it possible to build the original sequence from all of this rules
    - Can these rules result in more than 1 sequence

    In step "d" each number can become source only once and the edge (a rule) will be accessed and removed once. Therefore the time complexity
    will be O(V + E) where V is the count of distinct numbers and E is the total number of rules. Since at most each pair of numbers can give us
    one rule, we can conclude that the upper bond for the rules is O(N) where N is the count of numbers in all sequences. So the complexity will be
    O(V + N)

    The space complexity will be O(V + N) since we are storing all the rules for each number in an adjacency list.
    """
    if len(original_seq) == 0:
        return False

    graph = {}
    in_degree = {}

    # initialize the graph
    for sequence in sequences:
        for num in sequence:
            graph[num] = []
            in_degree[num] = 0

    # construct the graph
    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1

    # If we don't have ordering rules for all the numbers we can't construct the sequence
    if len(original_seq) != len(in_degree):
        return False

    # Find all sources, ex. all vertices with 0 in-degrees
    sources = deque()
    for key, value in in_degree.items():
        if value == 0:
            sources.append(key)
    sorted_order = []

    # step d
    # For each source, add it to the sorted order and substract 1 from all his children's in-degrees
    while sources:
        # If we have more than 1 source then we have more than 1 way to reconstruct our sequence
        if len(sources) > 1:
            return False
        # If the next source is different than the original sequence, can't have that
        if original_seq[len(sorted_order)] != sources[0]:
            return False
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original_seq)


@pytest.mark.parametrize(
    ("original_seq", "sequences", "expected"),
    (
        ([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]], True),
        ([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]], False),
        ([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]], True),
    ),
)
def test_can_construct(
    original_seq: List[int], sequences: List[List[int]], expected: bool
) -> None:
    assert can_construct(original_seq, sequences) == expected
