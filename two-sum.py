# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:49:38 2022

@author: ian50

class Solution(object):
    def twoSum(self, nums, target):

        :type nums: List[int]
        :type target: int
        :rtype: List[int]

"""
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
#%%
"""
Implement User-Defined-Functions(UDFs) in class

Learn Classes in Python in 4 min: https://www.youtube.com/watch?v=rJzjDszODTI
"""
Ans = Solution()
Ans.twoSum([1,2,3,4,5,6],11)
#%%

