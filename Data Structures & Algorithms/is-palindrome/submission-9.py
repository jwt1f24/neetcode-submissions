class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ""
        for char in s:
            if char.isalnum():
                alnum += char

        text = alnum.lower()
        if text != text[::-1]:
            return False
        
        return True