class Solution(object):
    def isPalindrome(self, x):

        if x<0:
            return False
        
        original=x
        rev=0

        while x>0:
            rev=rev*10 + x%10
            x=x//10
        return original==rev
        