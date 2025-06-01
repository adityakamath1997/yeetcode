class Solution(object):
    def strStr(self, haystack, needle):
        if haystack==needle:
            return 0
        n,m=len(needle),len(haystack)

        W=haystack[:n]

        for i in range(n,m):
            if W==needle:
                return i-n
            else:
                W=W[1:]+haystack[i]
                
        if W==needle:
            return m-n
        return -1
