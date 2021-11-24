from collections import deque
from typing import List

import pytest


def find_trees(nodes: int, edges: List[List[int]]) -> List[int]:
    """
    We are given an undirected graph that has characteristics to k-ary tree. In such graph, we can choose any node
    as the root to make a k-ary tree. The root of the tree with minimum height will be called minimum height tree.
    There can be multiple MHT's for a graph. For this problem we need to find them all.

    Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
    Output:[1, 2]
    Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the
    height of the trees with roots '1' or '2' is three which is minimum.

    Solution:
    From the above mentioned examples we can clearly see that any leaf node (node with only 1 edge) can never give us the MHT because its
    adjacent non-leaf nodes will always give MHT with a smaller height. All the adjacent non leaf nodes will consider the leaf as a subtree.
    Suppose we have a tree with root M and a height 5. Now if we take another node P and make M its subtree then the height of the overall
    tree will be 6(5+1). Now this whole tree can be considered a graph where P is leaf as it has only one edge (connection with M). This clearly shows
    that the leaf node (P) gives us a tree of height 6, whereas its adjacent non leaf node M gives us a tree with smaller height 5 since P will be a child
    of M.
    This gives us a strategy to find MHTs. Since leaves cannot give us MHTs we can remove them from the graph and remove their edges too. Once we remove the
    leafes, we will have new leaves. Since the new leaves cannot give us MHT, we will repeat the process and remove them from the graph too. We will prune
    the leaves until we are left with one or two nodes which will be the answer and the roots of MHT.

    We can implement the above process using the topological sort. Any node with only one edge (i.e. leaf) can be our source and in stepwise fashion, we can
    remove all sources from the graph to find new sources. We will repeat this process until we are left with one or two nodes in the graph.

    In step d each node can become a source only once and each edge will be accessed and removed once. Therefore, the time complexity of the above
    algorithm will be O(V+E) where V is the total nodes and E is the total number of edges.
    The space complexity will be O(V + E) since we are storing all of the edges for each node in adjacency list.
    """
    if nodes <= 0:
        return []

    if nodes == 1:
        return [0]

    # initialize the graph
    in_degree = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    # build the graph
    for edge in edges:
        n1, n2 = edge
        # since this is undirected graph add link to both the nodes
        graph[n1].append(n2)
        graph[n2].append(n1)
        in_degree[n1] += 1
        in_degree[n2] += 1

    leaves = deque()

    # find all leaves with 1 in degree
    for key, value in in_degree.items():
        if value == 1:
            leaves.append(key)

    # step d
    # Remove leaves level by level and substract each leave's children in degrees.
    # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
    # Any node that has already been a leaf cannot be the root of the MHT because
    # its adjacent non-leaf node will always be a better candidate
    total_nodes = nodes
    while total_nodes > 2:
        leaves_size = len(leaves)
        total_nodes -= leaves_size
        for i in range(leaves_size):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 1:
                    leaves.append(child)
    return list(leaves)


@pytest.mark.parametrize(
    ("nodes", "edges", "expected"),
    (
        (5, [[0, 1], [1, 2], [1, 3], [2, 4]], [1, 2]),
        (4, [[0, 1], [0, 2], [2, 3]], [0, 2]),
        (4, [[0, 1], [1, 2], [1, 3]], [1]),
    ),
)
def test_find_trees(nodes, edges, expected):
    assert find_trees(nodes, edges) == expected
