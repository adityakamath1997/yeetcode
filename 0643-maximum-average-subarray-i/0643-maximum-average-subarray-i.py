class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        W = 1.0 * sum(nums[0:k])
        max_avg = W
        for i in range(k, len(nums)):
            W = 1.0 * (W - nums[i - k] + nums[i])
            max_avg = max(max_avg, W)
        return max_avg / k

        