"""Given a set of investment projects with their respective profits, we need to find the most profitable projects. 
We are given an initial capital and are allowed to invest only in a fixed number of projects. 
Our goal is to choose projects that give us the maximum profit.

We can start an investment project only when we have the required capital. Once a project is selected,
we can assume that its profit has become our capital.

Example 1:

Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
Output: 6
Explanation:

    With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we selected our first project, our total capital will become 3 (profit + initial capital).
    With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.

After the completion of the two projects, our total capital will be 6 (1+2+3).

Example 2:

Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0, Number of Projects=3
Output: 8
Explanation:

    With ‘0’ capital, we can only select the first project, bringing out capital to 1.
    Next, we will select the second project, which will bring our capital to 3.
    Next, we will select the fourth project, giving us a profit of 5.

After selecting the three projects, our total capital will be 8 (1+2+5).

"""


import pytest
from typing import List
from heapq import *

# Since, at the most, all the projects will be pushed to both the heaps once,
#  the time complexity of our algorithm is O(NlogN + KlogN), where ‘N’ is the total number of projects and ‘K’
#  is the number of projects we are selecting.
# The space complexity will be O(N) because we will be storing all the projects in the heaps.
def find_maximum_capital(
    capital: List[int], profits: List[int], numberOfProjects: int, initialCapital: int
) -> int:
    min_capital_heap = []
    max_profit_heap = []

    # insert all project capitals to min heap
    for i in range(len(profits)):
        heappush(min_capital_heap, (capital[i], i))

    # try to find a total of number of projects best projects
    available_capital = initialCapital
    for _ in range(numberOfProjects):
        # find all projects that can be selected within the available capital and insert them in a max heap
        while min_capital_heap and available_capital >= min_capital_heap[0][0]:
            capital, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))

        if not max_profit_heap:
            break

        available_capital += -heappop(max_profit_heap)[0]

    return available_capital


"""
[0, 1, 2], [1, 2, 3], 2, 1 entries =>
How this works. We store all the capitals in min heap and their number like this
[(0, 0), (1, 1), (2, 2)] = min_capital_heap

we initiate available capital as the initial

we go through the min_capital_heap and if the available capital is higher or equal than the min_capital
we push those profits in max heap, and increase the available capital with the highest profit

1 >=  1st and 2nd items in the capital heap match this so their correspondant profits will be put in the max heap
max_profit_heap = [(-2, 1), (-1, 0)]

once we go out of while we check if we got items in max_profit_heap, if empty break

available capital will be = starting + max_profit_heap[0], that's 2 in this case

now are capital is 3 so we can continue with our process
"""


test_data = [
    ([0, 1, 2], [1, 2, 3], 2, 1, 6),
    ([0, 1, 2, 3], [1, 2, 3, 5], 3, 0, 8),
]


@pytest.mark.parametrize(
    "capitals, profits, num_projects, initial, expected", test_data
)
def test_find_maximum_capital(
    capitals: List[int],
    profits: List[int],
    num_projects: int,
    initial: int,
    expected: int,
):
    # for item in expected:
    assert my_func(capitals, profits, num_projects, initial) == expected
