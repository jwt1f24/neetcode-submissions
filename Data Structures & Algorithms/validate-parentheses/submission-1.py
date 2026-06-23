class Solution:
    def isValid(self, s: str) -> bool:
        pr = {')':'(', ']':'[', '}':'{'}
        stack = []

        # if input is empty
        if s == "":
            return False

        for c in s:
            if c in pr:
                # if stack is not empty & the last char is a closing bracket
                if stack and stack[-1] == pr[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        