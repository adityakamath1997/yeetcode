class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = defaultdict(int)
        
        # char -> count
        for char in magazine:
            seen[char] += 1

        for char in ransomNote:
            if char not in seen or seen[char] == 0:
                return False
            seen[char] -= 1

        return True