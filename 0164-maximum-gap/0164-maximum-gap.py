class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums=sorted(nums)
        max_diff=0
        if len(nums)<2:
            return 0
        elif len(nums)==2:
            return nums[-1]-nums[0]

        for i in range(1,len(nums)):
            max_diff=max(max_diff,nums[i]-nums[i-1])
        return max_diff


        