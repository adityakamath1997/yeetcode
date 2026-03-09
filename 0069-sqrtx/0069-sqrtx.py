class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x
        
        i, j = 0, x

        while i <= j:
            mid = (i + j) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1

        return i - 1