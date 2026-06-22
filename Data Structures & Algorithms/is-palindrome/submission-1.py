class Solution:
    def isPalindrome(self, s: str) -> bool:
        nospace = s.replace(" ", "")
        
        alnum = ""
        for char in nospace:
            if char.isalnum():
                alnum += char

        lower = alnum.lower()
        reverse = lower[::-1]
        if lower == reverse:
            return True
        else:
            return False