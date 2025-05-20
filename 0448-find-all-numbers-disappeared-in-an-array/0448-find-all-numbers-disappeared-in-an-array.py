class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set(range(1,n+1))
        print(seen)
        ans=[]
        for i in nums:
            if i in seen:
                seen.remove(i)
        return list(seen)
        