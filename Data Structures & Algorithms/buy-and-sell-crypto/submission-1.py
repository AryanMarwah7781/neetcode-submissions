class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                start_price=prices[i]
                if(start_price<prices[j] and prices[j]-start_price>max_profit):
                    max_profit=prices[j]-start_price
        return max_profit
                
        

        