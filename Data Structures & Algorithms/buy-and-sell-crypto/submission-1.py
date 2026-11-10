class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        maxDif = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxDif = max(maxDif, prices[r] - prices[l])
            r += 1
        return maxDif