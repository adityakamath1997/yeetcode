class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        temp = list()
        for num in range(1, len(nums) + 1):
            if num not in nums_set:
                temp.append(num)

        return temp