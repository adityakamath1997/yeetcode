class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=1.0*sum(nums[:k])

        max_sum=curr_sum/k

        for i in range(k,len(nums)):
            curr_sum=curr_sum+nums[i]-nums[i-k]
            max_sum=max(max_sum,curr_sum/k)

        return max_sum

        