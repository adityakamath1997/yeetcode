class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        summ1 = sum(nums)
        summ2 = n * (n-1) // 2
        return summ2 - summ1
        