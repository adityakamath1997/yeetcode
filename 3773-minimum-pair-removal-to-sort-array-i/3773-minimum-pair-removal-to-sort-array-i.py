class Solution(object):
    def minimumPairRemoval(self, nums):
        def check_ascending(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True
        
        ctr = 0
        
        while not check_ascending(nums):
            min_sum = float('inf')
            min_index = -1
            
            # Find the pair with the minimum sum
            for i in range(1, len(nums)):
                pair_sum = nums[i] + nums[i - 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # Merge the chosen pair
            nums[min_index - 1] = nums[min_index - 1] + nums[min_index]
            nums.pop(min_index)
            ctr += 1
        
        return ctr