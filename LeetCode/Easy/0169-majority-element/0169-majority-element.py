class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        temp = dict()
        count = n / 2

        for num in nums:
            temp[num] = temp.get(num, 0) + 1
            if temp[num] > count:
                return num

        