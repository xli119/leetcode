"""
Author: Xiaoyu Li
Created on 07/03/2018
flipping an image
"""


class Solution:
    def flip_and_invert(self, A):
        for row in A:
            for i in range(int((len(row))/2)):
                row[i], row[-i-1] = row[-i-1], row[i]
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return A

    def flip2(self, A):
        for row in A:
            for i in range(int(len(row)/2)):
                row[i], row[-i-1], 1-row[-i-1],1-row[i]
        return A


s = Solution()
print(s.flip2([[1,1,0], [1,0,1], [0,0,0]]))
print(s.flip2([[1,1,0,0], [0,1,1,0], [0,0,0,1], [1,0,1,0]]))

# time complexity: O(N)
# space complexity: O(1)
