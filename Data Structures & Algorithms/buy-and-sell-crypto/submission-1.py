class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < bought:
                bought = prices[i]
            if prices[i] > bought:
                profit = max(profit, prices[i] - bought)
        return profit

            
        