class Solution(object):
    def maximumProduct(self, nums):
        a=sorted(nums)

        p1=a[-1]*a[-2]*a[-3]
        p2=a[0]*a[1]*a[-1]

        return max(p1,p2)
        