"""
Author: Xiaoyu Li
Created on 7/5/2018
Array 561 Array partition1
"""

def array_pair_sum(nums):
    exist = dict()
    for i in nums:
        exist[i] = exist.get(i, 0) + 1

    sum = 0
    is_even = False
    for n, freq in exist.items():
        if freq:
            freq = freq - 1 if is_even else freq
            if freq & 1:
                sum += ((freq // 2) + 1) * n
                is_even = True
            else:
                sum += (freq // 2) * n
                is_even = False
    return sum


def array_pair_sum2(nums):
    return sum(sorted(nums)[::2])


print(array_pair_sum([1,2,3,4]))
print(array_pair_sum2([1,2,3,4]))


