class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        n = len(nums)
        target = n // 2

        for num in nums:
            seen[num] += 1
            if seen[num] > target:
                return num
