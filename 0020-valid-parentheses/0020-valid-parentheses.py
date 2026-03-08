class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        lookup= {")": "(", "}": "{", "]": "["}
        stack = []

        for val in s:
            if val in lookup.values():
                stack.append(val)
            elif stack and lookup[val] == stack[-1]:
                stack.pop()
            else:
                return False

        
        return not stack
            
        