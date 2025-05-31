class Solution(object):
    def arrayPairSum(self, nums):
        new_nums=sorted(nums)
        s=0
        for i in range(1,len(nums),2):
            s+=min(new_nums[i],new_nums[i-1])

        return s

        