class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        for i in range(len(s)):
            print(s[i])
            if i+1<len(s) and m[s[i]]<m[s[i+1]]:
                sum-=m[s[i]]
            else:
                sum+=m[s[i]]
        return sum