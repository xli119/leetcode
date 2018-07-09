"""
Author: Xiaoyu Li
Created on 7/9/2018
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
"""
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = []
        ret = []
        for i in nums:
            if i in new:
                ret.append(i)
            if i not in new:
                new.append(i)

        return ret

    def findDuplicates2(self, nums):
        ret = []
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                ret.append(abs(i))
            else:
                nums[idx] = - nums[idx]
        return ret
    