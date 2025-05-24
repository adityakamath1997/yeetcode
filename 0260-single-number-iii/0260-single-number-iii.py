class Solution(object):
    def singleNumber(self, nums):
        seen={}
        ans=[]
        for val in nums:
            seen[val]=seen.get(val,0)+1

        for val,idx in seen.items():
            if idx==1:
                ans.append(val)
        return ans
        