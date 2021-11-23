from collections import deque
from typing import Dict, List

import pytest


def print_orders(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks
    which need to be completed before it can be scheduled. Given the number of tasks and a list
    of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

    Can use a recursive approach with Backtracking to consider all sources at any step
    """
    if tasks <= 0:
        return []

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for edge in prerequisites:
        parent, child = edge
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()

    for key, value in in_degree.items():
        if value == 0:
            sources.append(key)

    sorted_order = []
    print_all_topological_sorts(graph, in_degree, sources, sorted_order)


def print_all_topological_sorts(
    graph: Dict, in_degree: Dict, sources: deque, sorted_order: List
):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            # male copy of sources
            sources_for_next_call = deque(sources)
            # remove current source
            sources_for_next_call.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

            print_all_topological_sorts(
                graph, in_degree, sources_for_next_call, sorted_order
            )
            # backtrack, remove the vertex from the sorted order and put all of its children back to consider
            # the next source instead of the current vertex
            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

    # if sorted order doesn't contain all the tasks either we have cyclic dependency or
    # we have not yet processed all the tasks in the recursive call
    if len(sorted_order) == len(in_degree):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


if __name__ == "__main__":
    main()
