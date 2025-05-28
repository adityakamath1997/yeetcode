class Solution(object):
    def isPalindrome(self, s):
        new_s=""

        for char in s:
            if char.isalnum():
                new_s+=char.lower()
        l=0
        r=len(new_s)-1

        while l<r:
            if new_s[l].lower()!=new_s[r].lower():
                return False
            l+=1
            r-=1
        return True
        