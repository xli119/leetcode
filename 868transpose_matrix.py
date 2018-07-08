"""
Author: Xiaoyu Li
Created on 7/8/2018
Given a matrix A, return the transpose of A.
"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i >= j:
                    A[i][j], A[j][i] = A[j][i], A[i][j]
        return A
