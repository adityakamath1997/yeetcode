class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        insert = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[insert - 1]:
                nums[insert] = nums[i]
                insert += 1

        return insert