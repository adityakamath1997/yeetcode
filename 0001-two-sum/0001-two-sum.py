class Solution(object):
    def twoSum(self, nums, target):
        m={}
        for idx, val in enumerate(nums):
            diff=target-val
            if diff in m:
                return [m[diff],idx]
            m[val]=idx
        return []