class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l=0
        longest=0
        sett=set()
        n=len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            longest=max(longest,(r-l)+1)
            sett.add(s[r])
        return longest


        