class Solution(object):
    def intersect(self, nums1, nums2):
        ct=Counter(nums1)
        res=[]


        for num in nums2:
            if ct[num]>0:
                res.append(num)
                ct[num]-=1
        return res
        