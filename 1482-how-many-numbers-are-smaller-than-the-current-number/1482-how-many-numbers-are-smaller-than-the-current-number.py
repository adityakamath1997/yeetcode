class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=sorted(nums)
        m={}
        ans=[]

        for idx,val in enumerate(temp):
            if val not in m:
                m[val]=idx

        for num in nums:
            ans.append(m[num])

        return ans
        