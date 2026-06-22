class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # anagrams must have same word length
        
        d1 = dict()
        for char in s:
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1

        d2 = dict()
        for char in t:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1
        
        # check if key exists w/o accessing dict first, then check if both keys have same values
        for key in d1:
            if key not in d2 or d1[key] != d2[key]: 
                return False

        return True
            