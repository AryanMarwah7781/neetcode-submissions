class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        result = 0

        for r in range(1,len(prices)):
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy
            result = max(result, profit)
            if sell < buy:
                l = r
        
        return result


