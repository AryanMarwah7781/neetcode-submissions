class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in brackets:
                if stack:
                    last = stack.pop()
                    if not last == brackets[c]:
                        return False
                else: return False
            else:
                stack.append(c)
        
        return True if not stack else False
