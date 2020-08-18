"""Because a renovation of all of the buildings is planned, we want to cover them with rectangular banners
until the renovations are finished. Of course, to cover a building, the banner has to be at least as high
as the building. We can cover more than one building with a banner if it is wider than 1.

For example, to cover buildings of heights 3, 1, 4 we could use a banner of size 4×3 (i.e. of height 4 and width 3), marked here in blue:

We can order at most two banners and we want to cover all of the buildings. Also, we want to minimize the amount 
of material needed to produce the banners.

What is the minimum total area of at most two banners which cover all of the buildings?


1. Given H = [3, 1, 4], the function should return 10. The result can be achieved by covering the first two buildings with a banner
 of size 3×2 and the third building with a banner of size 4×1:
"""
from typing import List
import pytest
import math


def find_min_area(buildings: List[int]) -> int:
    n = len(buildings)
    max_from_left = [0] * (n + 1)
    max_from_right = [0] * (n + 1)
    current_max = 0

    for i in range(n):
        current_max = max(current_max, buildings[i])
        max_from_left[i + 1] = current_max

    current_max = 0
    for i in range(n - 1, -1, -1):
        current_max = max(current_max, buildings[i])
        max_from_right[i] = current_max

    print("max left: ", max_from_left)
    print("max right: ", max_from_right)

    result = math.inf
    for i in range(n + 1):
        print("max from left: ", max_from_left[i] * i)
        print("max from right: ", max_from_right[i] * (n - i))

        result = min(result, max_from_left[i] * i + max_from_right[i] * (n - i))
        print("result: ", result)
        print("____________________-")
    return result


find_min_area([1, 1, 7, 6, 6, 6])

test_data = [
    ([3, 1, 4], 10),
    ([5, 3, 2, 4], 17),
    ([7, 7, 3, 7, 7], 35),
    ([1, 1, 7, 6, 6, 6], 30),
]


@pytest.mark.parametrize("input_arr, expected", test_data)
def test_find_min_area(input_arr, expected):
    assert find_min_area(input_arr) == expected
