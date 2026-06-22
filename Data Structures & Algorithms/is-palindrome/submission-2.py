class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ""
        for char in s:
            if char.isalnum():
                alnum += char

        lower = alnum.lower()
        reverse = lower[::-1]
        if lower == reverse:
            return True
        else:
            return False