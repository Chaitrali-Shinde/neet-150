class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy= prices[0]
        profit=0
        for i in range(1, len(prices)):
            p= prices[i]- buy
            profit= max(p, profit)
            #print()
            buy= min(prices[i], buy)
        return profit

        