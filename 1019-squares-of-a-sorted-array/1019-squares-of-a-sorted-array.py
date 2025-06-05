class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        sorted_arr = [0] * len(nums)
        ptr = len(nums) - 1
        L = 0
        R = len(nums) - 1

        while L <= R:
            if abs(nums[L]) >= abs(nums[R]):
                sorted_arr[ptr] = (nums[L] ** 2)
                L += 1
            else:
                sorted_arr[ptr] = nums[R] ** 2
                R -= 1
            ptr -= 1
        return sorted_arr
            

        
        