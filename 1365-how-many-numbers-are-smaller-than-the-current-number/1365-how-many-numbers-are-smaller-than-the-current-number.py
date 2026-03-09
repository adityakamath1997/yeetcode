class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort = sorted(nums)
        temp_dict = dict()
        ans = list()
        for idx, num in enumerate(nums_sort):
            if num not in temp_dict:
                temp_dict[num] = idx
        for num in nums:
            ans.append(temp_dict[num])
        return ans



        