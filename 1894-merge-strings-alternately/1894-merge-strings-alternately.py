class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol=""
        l1=len(word1)
        l2=len(word2)
        l=min(l1,l2)
        for i in range(l):
            sol+=word1[i]+word2[i]
        sol+=word1[l:l1]+word2[l:l2]
        return sol
        