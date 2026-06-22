class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for n in nums:
            if n in myset:
                return True # contains duplicate
            else:
                myset.add(n)
                
        return False # no duplicate
            