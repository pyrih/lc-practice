class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        max_profit = 0

        for i in range(days - 1):
            for j in range(i + 1, days - 1):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit