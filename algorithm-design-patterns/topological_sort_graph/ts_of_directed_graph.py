"""
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of 
its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

         3
        / \ 
       /   2
        0  /\
             1   

Example 2:

Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1 

Example 3:

Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0
 
There are other valid topological ordering of the graph too.

Solution #

The basic idea behind the topological sort is to provide a partial ordering among the vertices of the graph 
such that if there is an edge from U to V then U≤V i.e., U comes before V in the ordering. Here are a few 
fundamental concepts related to topological sort:

    Source: Any node that has no incoming edge and has only outgoing edges is called a source.

    Sink: Any node that has only incoming edges and no outgoing edge is called a sink.

    So, we can say that a topological ordering starts with one of the sources and ends at one of the sinks.

    A topological ordering is possible only when the graph has no directed cycles, i.e. if the graph is a 
    Directed Acyclic Graph (DAG). If the graph has a cycle, some vertices will have cyclic dependencies which
    makes it impossible to find a linear ordering among vertices.

To find the topological sort of a graph we can traverse the graph in a Breadth First Search (BFS) way.
We will start with all the sources, and in a stepwise fashion, save all sources to a sorted list. 
We will then remove all sources and their edges from the graph. After the removal of the edges, we will have 
new sources, so we will repeat the above process until all vertices are visited.
"""
from collections import deque
import pytest


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjancency list graph

    # build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into it's parents list
        in_degree[child] += 1  # increment childs in degree

    # find all sources i.e. all vertices with 0 in degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # for each source add it to the sorted order and substract one from all of its children in degrees
    # if a childs in degree is zero add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []
    return sorted_order


test_data = [
    (4, [[3, 2], [3, 0], [2, 0], [2, 1]], [3, 2, 0, 1]),
    (5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]], [4, 2, 3, 0, 1]),
    (
        7,
        [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]],
        [5, 6, 3, 4, 0, 2, 1],
    ),
]


@pytest.mark.parametrize("vertices, edges, expected", test_data)
def test_topological_sort(vertices, edges, expected):
    assert topological_sort(vertices, edges) == expected


def main():
    print(
        "Topological sort: "
        + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    )
    print(
        "Topological sort: "
        + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    )
    print(
        "Topological sort: "
        + str(
            topological_sort(
                7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
            )
        )
    )


main()
