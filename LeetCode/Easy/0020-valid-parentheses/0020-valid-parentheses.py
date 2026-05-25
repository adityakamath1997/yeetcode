class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in temp.values():
                stack.append(char)
            elif char in temp.keys():
                if not stack or temp[char] != stack.pop():
                    return False
        return not stack