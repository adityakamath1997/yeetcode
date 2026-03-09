class Solution:
    def isPalindrome(self, s: str) -> bool:

        stripped_s = ""
        
        for char in s:
            if char.isalnum():
                stripped_s += char

        return stripped_s.lower() == stripped_s.lower()[::-1]
        