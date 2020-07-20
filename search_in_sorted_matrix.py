"""You are given a matrix of distinct integers and a target integer. Each row and columns are sorted
Write a function that returns the indexes of the target if inside the matrix else [-1, -1]
"""

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]

