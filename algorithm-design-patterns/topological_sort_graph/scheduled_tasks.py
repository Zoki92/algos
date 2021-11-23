from collections import deque

import pytest


def is_scheduling_possible(tasks, prerequisites):
    """
    There are N tasks labeled from 0 to N-1. Each task can have some prerequisite tasks which need to be completed
    before it can be scheduled. Given the number of tasks and a list of prerequisites pairs, find out if it
    is possible to schedule all the tasks.

    Tasks = 3
    Prerequisites = [0, 1], [1, 2]
    Explanation: To execute task 1, task 0 needs to finish first. Similarly task 1 needs to finish before task 2 can be scheduled. One
    possible scheduling is [0,1,2]

    Solution:
    The task is asking if it is possible to find topological ordering of the given tasks. The tasks are equivalent to the vertices and the
    prerequisites are the edges. If the ordering doesn't include all the tasks then we have some cyclic dependencies.

    To find the topological sort of a graph we can traverse in a Breadth First Search way. We will start with all the sources and in stepwise
    fashion save all sources to a sorted list. We will then remove all the sources and their edges from the graph. After the removal of the edges
    we will have new sources, so we will repeat the process until all the vertices are visited.

    In last step, each task can become source only once, and each edge, will be accessed and removed once. The time complexity of the algorithm
    will be O(V+E), where V is the total number of tasks and E is the total number of prerequisites.
    The space complexity will be O(V+E) since we are storing all the prerequisites for each task in an adjacency list.
    """
    if tasks <= 0:
        return []

    sorted_order = []

    # initialise a graph and degree of childs
    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}

    # construct the graph
    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    # find all the sources
    for key, value in in_degree.items():
        if value == 0:
            sources.append(key)

    # repeat process until queue is empty
    while sources:
        vertex = sources.popleft()
        # add the source to the sorted list
        sorted_order.append(vertex)
        # get all the children from the graph
        for child in graph[vertex]:
            # decrement the degree of the child in the graph
            in_degree[child] -= 1
            # if child's degree becomes zero, add it to the sources
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == tasks


@pytest.mark.parametrize(
    ("tasks, prerequisites, expected"),
    (
        (3, [[0, 1], [1, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
        (6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]], True),
    ),
)
def test_is_scheduling_possible(tasks, prerequisites, expected):
    assert is_scheduling_possible(tasks, prerequisites) == expected
