class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']': '['}
        stack = list()

        for char in s:
            if char in char_map.values():
                stack.append(char)
            elif char in char_map:
                if not stack or char_map[char] != stack.pop():
                    return False

        return not stack
        