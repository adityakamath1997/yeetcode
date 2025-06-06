class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        running_sum = 0
        L = 0
        length = 10 ** 6
        for R in range(len(nums)):
            running_sum += nums[R]
            while running_sum >= target:
                W = R - L + 1
                length = min(length, W)
                running_sum -= nums[L]
                L += 1
        return 0 if length == 10 ** 6 else length
