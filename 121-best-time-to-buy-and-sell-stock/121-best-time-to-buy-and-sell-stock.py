class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l, r = 0, 1
        bestPrice = 0
        while(r < len(prices)):
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                bestPrice = max(bestPrice, prices[r]-prices[l])
                r += 1
        return bestPrice