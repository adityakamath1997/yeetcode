class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in temp:
                return [i, temp[diff]]
            temp[nums[i]] = i

        return []
            
            
        