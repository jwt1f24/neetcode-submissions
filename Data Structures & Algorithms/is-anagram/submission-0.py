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
        
        for key in d1:
            if key not in d2: # check if key exists w/o accessing dict
                return False
            if d1[key] != d2[key]: # if both keys have different value
                return False

        return True
            