class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = dict()
        length = 0
        odd = False

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in count.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd = True
        
        if odd:
            length += 1

        return length
        