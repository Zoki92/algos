"""
Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.
The Euclidean distance of a point P(x,y) from the origin can be calculated through the following formula:

sqrt{x^2 + y^2}
Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""
import pytest
from typing import List
from heapq import *
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin > other.distance_from_origin

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def distance_from_origin(self):
        return self.x * self.x + self.y * self.y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end="")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# The time complexity of this algorithm is (N∗logK) as we iterating all points and pushing them into the heap.
# The space complexity will be O(K) because we need to store ‘K’ point in the heap.
def find_closest_points(points: List[Point], k: int) -> List:
    min_heap = []
    for i in range(k):
        heappush(min_heap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin < min_heap[0].distance_from_origin:
            heappop(min_heap)
            heappush(min_heap, points[i])
    return list(min_heap)


test_data = [
    ([Point(1, 2), Point(1, 3)], 1, [Point(1, 2)]),
    ([Point(1, 3), Point(3, 4), Point(2, -1)], 2, [Point(1, 3), Point(2, -1)]),
]


@pytest.mark.parametrize("points, k, expected", test_data)
def test_find_closest_points(points, k, expected):
    assert find_closest_points(points, k) == expected
