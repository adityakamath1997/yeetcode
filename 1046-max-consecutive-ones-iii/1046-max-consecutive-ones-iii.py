class Solution(object):
    def longestOnes(self, nums, k):
        L = R = 0
        count = k
        max_len = 0
        while R < len(nums):

            if nums[R] == 1:
                R += 1
                max_len = max(max_len, R - L )
            
            elif nums[R] == 0 and count > 0:
                R += 1
                count -= 1
                max_len = max(max_len, R - L )
            elif nums[R] == 0 and count == 0:
                if nums[L] == 0:
                    count += 1
                    L += 1
                elif nums[L] == 1:
                    L += 1
        return max_len
