class Solution(object):
    def lengthOfLongestSubstring(self, s):
        L=0
        seen=set()
        longest=0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[L])
                L+=1
            seen.add(s[r])
            longest=max(longest,(r-L)+1)
        return longest