class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Sol 1 - O(nlogn)

        ans = [i ** 2 for i in nums]
        ans.sort()
        return ans
        