class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = 0
        minAmount = prices[0]
        for i in range(len(prices)):
            profit = max(prices[i] - minAmount, profit)
            minAmount = min(prices[i], minAmount)
        return profit
