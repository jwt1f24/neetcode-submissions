class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # divide and round off to nearest full number
            if nums[mid] == target:
                return mid

            # if number is smaller than target, move rightwards, and vice versa
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # if target not found in array, return -1
        return -1

        # time comp. = O(log n), var 'mid' divides 2 vars which skips remaining values
        # space comp. = O(1), var 'left' & 'right' are constant