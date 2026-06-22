class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ""
        for char in s:
            if char.isalnum():
                alnum += char

        if alnum.lower() != alnum.lower()[::-1]:
            return False
        
        return True