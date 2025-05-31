class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        res=""
        max_length=0

        for i in range(n):
            L,R=i,i

            while L>=0 and R<n and s[L]==s[R]:
                if (R-L+1)>max_length:
                    res=s[L:R+1]
                    max_length=R-L+1
                L-=1
                R+=1
        
            
            L,R=i,i+1

            while L>=0 and R<n and s[L]==s[R]:
                if (R-L+1)>max_length:
                    res=s[L:R+1]
                    max_length=R-L+1
                L-=1
                R+=1
        return res