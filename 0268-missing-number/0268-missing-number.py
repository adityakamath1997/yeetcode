class Solution(object):
    def missingNumber(self, nums):
        L=len(nums)

        return sum(range(0,L+1))-sum(nums) 
