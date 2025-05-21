class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        L=0
        R=0
        ans=''
        while L<len(s) and R<len(t):
            if s[L]==t[R]:
                ans+=t[R]
                L+=1
                R+=1
            elif s[L]!=t[R]:
                R+=1
        print(ans)
        return ans==s
        