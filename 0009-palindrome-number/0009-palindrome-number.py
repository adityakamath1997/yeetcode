class Solution(object):
    def isPalindrome(self, x):
        

        def reverse(n):
            q=0
            r=0
            while n>0:
                r=n%10
                q=q*10+r
                n=n//10
            return q
        if x==reverse(x):
            return True
        return False
        