class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        list_sum = sum(nums)
        num_sum = sum(range(0,len(nums)+1))

        return num_sum - list_sum