class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length=0
        length=0
        for i in nums:
            if i==0:
                length=0
            if i==1:
                length+=1
            max_length=max(length,max_length)
        return max_length
            