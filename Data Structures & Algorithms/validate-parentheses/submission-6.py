class Solution:
    def isValid(self, s: str) -> bool:
        pr = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in pr:
                # if stack is not empty & the last char is a closing bracket
                if stack and stack[-1] == pr[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # append if stack is empty, or first char is opening bracket
        
        # True if stack is empty
        return True if not stack else False
        