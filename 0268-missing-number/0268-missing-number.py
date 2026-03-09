class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        vals = len(nums)
        temp = set(range(vals + 1))
        nums_set = set(nums)

        return int(list(temp - nums_set)[0])