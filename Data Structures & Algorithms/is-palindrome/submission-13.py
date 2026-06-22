class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for char in s.lower():
            if char.isalnum():
                text += char

        if text != text[::-1]:
            return False
        
        return True