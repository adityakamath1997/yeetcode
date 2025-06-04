class Solution(object):
    def isPalindrome(self, s):
        new_s = ""

        for char in s:
            if char.isalnum():
                new_s += char.lower()
        print(new_s)
        low = 0
        high = len(new_s) - 1

        while low <= high:
            if new_s[low] != new_s[high]:
                return False
            low += 1
            high -= 1
        return True
        