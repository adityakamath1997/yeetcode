class Solution(object):
    def singleNumber(self, nums):

        seen = Counter(nums)

        for key, value in seen.items():
            if value != 3:
                return key
        