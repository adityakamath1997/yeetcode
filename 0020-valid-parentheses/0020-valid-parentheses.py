class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in hash_map.values():
                stack.append(char)
            elif char in hash_map.keys():
                if not stack or hash_map[char] != stack.pop():
                    return False
        return not stack