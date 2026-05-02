class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        buying_p=0
        selling_p=1
        while selling_p<len(prices):
            if prices[buying_p]<prices[selling_p]:
                profit=prices[selling_p]-prices[buying_p]
                maxprofit=max(maxprofit,profit)
            else:
                buying_p=selling_p
            selling_p+=1
        return maxprofit

        