class Solution(object):
    def lengthOfLongestSubstring(self, s):
        L=0
        seen=set()
        longest=0
        n=len(s)

        for R in range(n):
            while s[R] in seen:
                seen.remove(s[L])
                L+=1
            seen.add(s[R])
            W=(R-L)+1
            longest=max(longest,W)
        return longest