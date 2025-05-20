class Solution:
    def mySqrt(self, x: int) -> int:
        L=0
        R=x
        result=0
        while L<=R:
            mid=(L+R)//2
            if x>(mid*mid):
                L=mid+1
                result=mid
            elif x<(mid*mid):
                R=mid-1
            elif x==(mid*mid):
                return mid
        return result
        