class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=0.0
        for i in range(k):
            curr_sum+=nums[i]

        max_sum=curr_sum/k

        for i in range(k,len(nums)):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]
            max_sum=max(max_sum,curr_sum/k)

        return max_sum

        