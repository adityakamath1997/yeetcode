class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = defaultdict(int)
        odd = False
        count = 0

        for char in s:
            seen[char] += 1

        for value in seen.values():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                odd = True

        count += 1 if odd else 0

        return count

        