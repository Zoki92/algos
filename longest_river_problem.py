"""River sizes problem
You are given matrix of m x n filled with 0 and 1s, and each 1 represents part of a river. A river
consists of any number of 1s that are either horizontally or vertically adjacent, but no diagonally.
The number of adjacent 1s form the size of the river. A river can twist, in other words it can have
the shape L.
Write a function that returns an array of the sizes of all rivers represented in the input matrix.
"""
# Space O(m * n) or O(N) where N is the number of elements in the matrix
# Time O(m * n) essentially we go through every item in the matrix
def riverSizes(matrix):
    size_array = []
    visited = [[False for n in row]for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_graph(i, j, matrix, visited, size_array)
    return size_array

def traverse_graph(i, j, matrix, visited, size_array):
    current_river_size = 0
    unexplored = [[i, j]]
    while len(unexplored):
        current_node = unexplored.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_river_size += 1
        unexplored_neighbours = get_unexplored_neighbours(i, j, matrix, visited)
        for neighbour in unexplored_neighbours:
            unexplored.append(neighbour)
    if current_river_size > 0:
        size_array.append(current_river_size)


def get_unexplored_neighbours(i, j, matrix, visited):
    unexplored = []
    if i > 0 and not visited[i-1][j]:
        unexplored.append([i-1, j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unexplored.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unexplored.append([i, j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unexplored.append([i, j+1])
    return unexplored


input_array = [
  [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
  [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
  [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]

print(riverSizes(input_array))