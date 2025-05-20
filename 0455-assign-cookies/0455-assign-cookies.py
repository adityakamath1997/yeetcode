class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        l=0
        r=0
        ct=0

        while l<len(g) and r<len(s):
            if s[r]>=g[l]:
                ct+=1
                l+=1
                r+=1
            elif s[r]<g[l]:
                r+=1
        return ct

