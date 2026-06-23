class Solution:
    def isValid(self, s: str) -> bool:
        pr = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in pr:
                # if stack is not empty & the top elem matches closing bracket in hashmap
                if stack and stack[-1] == pr[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # append if stack is empty, or first char is opening bracket
        
        # true if stack is empty, false otherwise
        return not stack
        