class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy= prices[0]
        # profit=0
        # for i in range(1, len(prices)):
        #     p= prices[i]- buy
        #     profit= max(p, profit)
        #     #print()
        #     buy= min(prices[i], buy)
        # return profit

        l, r= 0, 1
        maxProfit=0
        while r< len(prices):
            if prices[l]<prices[r]:
                maxProfit= max(maxProfit, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return maxProfit

                

        