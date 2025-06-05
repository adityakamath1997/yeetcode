class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        L = 0
        R = 0

        while R < len(prices):
            max_profit = max(max_profit, prices[R] - prices[L])
            if prices[L] >= prices[R]:
                L = R
                R += 1
            else:
                R += 1
                
        return max_profit
        