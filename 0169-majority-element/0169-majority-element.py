class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums) // 2
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > n:
                return num
        