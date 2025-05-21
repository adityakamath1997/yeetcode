class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L,R=0,1

        while R<=len(nums)-1:
            if nums[L]==0 and nums[R]!=0:
                nums[L],nums[R]=nums[R],nums[L]
                L+=1
                R+=1
            elif nums[L]==0 and nums[R]==0:
                R+=1
            else:
                L+=1
                R+=1

        