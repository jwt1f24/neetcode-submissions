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
            if buy >= i:
                buy = i

        if maxpft < 0:
            return 0
        else:
            return maxpft

        # time comp. = O(n)
        # space comp. = O(1)