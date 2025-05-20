class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digital_sum(n):
            total=0
            while n>0:
                total+=n%10
                n//=10
            return total
        
        for i in range(len(nums)):
            if i==digital_sum(nums[i]):
                return i
        return -1