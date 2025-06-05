class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        L = 0
        R = 0

        while L < len(s) and R < len(t):
            if s[L] == t[R]:
                L += 1
                R += 1
            else:
                R += 1

        return L == len(s)
        