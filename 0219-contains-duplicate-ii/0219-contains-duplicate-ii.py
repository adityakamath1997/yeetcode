class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m={}

        for idx, num in enumerate(nums):
            if num in m and abs(idx-m[num])<=k:
                return True
            m[num]=idx
        return False
        