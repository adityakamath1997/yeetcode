class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        ans=0
        l=0
        r=0
        if not nums:
            return []
        if len(nums)==1:
            return [f"{nums[0]}"]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                r=r+1
            else:
                if l!=r:
                    res.append(f"{nums[l]}->{nums[r]}")
                elif l==r:
                    res.append(f"{nums[l]}")
                r=r+1
                l=r
        if l != r:
            res.append(f"{nums[l]}->{nums[r]}")
        else:
            res.append(f"{nums[l]}")

        return res
