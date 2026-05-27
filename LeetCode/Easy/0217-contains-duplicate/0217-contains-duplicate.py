class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = dict()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] >= 2:
                return True

        return False