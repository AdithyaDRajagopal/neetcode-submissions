class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
                continue

            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit