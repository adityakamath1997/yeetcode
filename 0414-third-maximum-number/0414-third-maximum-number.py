class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans=0
        nums=list(set(nums))
        print(type(nums))
        print(nums)
        if len(nums)<3:
            return max(nums)
        else:
            nums=sorted(nums)
            ans=nums[-3]
        return ans
        
        