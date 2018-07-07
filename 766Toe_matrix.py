"""
Author: Xiaoyu Li
Created on 7/6/2018
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""


def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """

    for idxr in range(1, len(matrix)):
        for idxc in range(1, len(matrix[0])):
            if idxc >= idxr:
                if matrix[idxr][idxc] != matrix[0][idxc - idxr]:
                    return False
            else:
                if matrix[idxr][idxc] != matrix[idxr - idxc][0]:
                    return False

    return True


print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,2,2]]))