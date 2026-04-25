class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            
            if profit < 0:
                l = r
                continue
            
            maxProfit = max(profit, maxProfit)
        
        return maxProfit
            