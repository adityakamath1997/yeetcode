class Solution(object):
    def missingNumber(self, nums):
        L=len(nums)

        for i in range(0,L+1):
            if i not in nums:
                return i

