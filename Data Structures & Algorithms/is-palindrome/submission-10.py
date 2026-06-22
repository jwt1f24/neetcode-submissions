class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        alnum = ""
        for char in text:
            if char.isalnum():
                alnum += char

        if alnum != alnum[::-1]:
            return False
        
        return True