class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = dict()

        if len(s) != len(t):
            return False

        for char in s:
            temp[char] = temp.get(char, 0) + 1

        for char in t:
            if char not in temp or temp[char] == 0:
                return False
            else:
                temp[char] -= 1

        return True

        