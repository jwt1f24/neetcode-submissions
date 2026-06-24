class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxpft = 0

        for i in prices:
            # current profit
            profit = i - buy
            if maxpft < profit:
                maxpft = profit
            
            # find min value for buy price
            if buy > i:
                buy = i
        return maxpft

        # time comp. = O(n), day count grows based on input size
        # space comp. = O(1), var 'buy' & 'maxpft' are constant