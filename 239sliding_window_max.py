"""
Author: Xiaoyu Li
Created on 7/14/2018
Given an array nums, there is a sliding window of size k which is moving from the very left of the array
 to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
 by one position. Return the max sliding window.
"""

import collections


def sliding_window_max(nums, k):
    l = len(nums) - k + 1
    ret = []
    for i in range(l):
        ret.append(max(nums[i], nums[i+1], nums[i+2]))
    return ret


def sliding_window_max2(nums, k):
    d = collections.deque()
    ret = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            ret += nums[d[0]],
    return ret

print(sliding_window_max2([1,3,-1,-3,5,3,6,7], 3))
