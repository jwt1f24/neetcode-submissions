class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for char in s:
            if char.isalnum():
                text += char.lower()

        if text != text[::-1]:
            return False
        
        return True