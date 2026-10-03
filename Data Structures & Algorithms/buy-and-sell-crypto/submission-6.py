class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        profit=0
        min_i=arr[0]
        for i in range(1,len(arr)):
            profit1=0
            if arr[i] > min_i:
                profit1=arr[i]-min_i
            else:
                min_i=arr[i]
            profit=max(profit1,profit)
        final_profit =profit if profit >0 else 0
        return final_profit





        