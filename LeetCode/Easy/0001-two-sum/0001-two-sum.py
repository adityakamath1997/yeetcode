class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in temp:
                return [i, temp[diff]]
            temp[num] = i
        