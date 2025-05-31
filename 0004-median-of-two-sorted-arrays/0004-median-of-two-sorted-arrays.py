class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        num=nums1+nums2
        num.sort()
        mid=len(num)//2
        if len(num)%2==1:
            return float(num[mid])
        else:
            return float((num[mid-1]+num[mid])/2.0)
        