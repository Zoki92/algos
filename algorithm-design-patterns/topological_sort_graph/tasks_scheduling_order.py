from collections import deque

import pytest


def find_order(tasks, prerequisites):
    """
    There are N tasks, labeled from 0 to N-1. Each task can have some prerequisite tasks which need to be completed,
    before it can be scheduled. Given the number of tasks and a list of prerequisites pairs, write a method to find
    the ordering of tasks we should pick to finish all tasks.

    In step ‘d’, each task can become a source only once and each edge (prerequisite) will be accessed and removed once.
    Therefore, the time complexity of the above algorithm will be O(V+E)O(V+E), where ‘V’ is the total number of tasks
    and ‘E’ is the total number of prerequisites.

    Space complexity
    The space complexity will be O(V+E)O(V+E), since we are storing all of the prerequisites for each task in an adjacency list.
    """
    if tasks <= 0:
        return []
    sorted_order = []

    # initialise the graph
    graph = {i: [] for i in range(tasks)}
    # initialise the count of degrees
    in_degrees = {i: 0 for i in range(tasks)}

    # build the graph
    for edge in prerequisites:
        parent, child = edge
        graph[parent].append(child)
        in_degrees[child] += 1

    sources = deque()

    # find all sources
    for key, value in in_degrees.items():
        if value == 0:
            sources.append(key)

    # step d
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    if len(sorted_order) != tasks:
        return []

    return sorted_order


@pytest.mark.parametrize(
    ("tasks", "prerequisites", "expected"),
    (
        (3, [[0, 1], [1, 2]], [0, 1, 2]),
        (3, [[0, 1], [1, 2], [2, 0]], []),
        (6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]], [0, 1, 4, 3, 2, 5]),
    ),
)
def test_find_order(tasks, prerequisites, expected):
    assert find_order(tasks, prerequisites) == expected
