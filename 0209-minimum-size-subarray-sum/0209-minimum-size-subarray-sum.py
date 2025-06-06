class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        running_sum = 0
        L = 0
        min_length = 10 ** 6
        for R in range(len(nums)):
            running_sum += nums[R]
            while running_sum >= target:
                W = (R - L) + 1
                min_length = min(min_length, W)
                running_sum -= nums[L]
                L += 1
        
        if min_length == 10 ** 6:
            return 0
        else:
            return min_length
