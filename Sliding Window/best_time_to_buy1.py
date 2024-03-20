class Solution:
    def maxProfit(self, prices):
        maxi = 0
        l, r = 0, 1
        
        while r < len(prices):
            maxi = max(maxi, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            else:
                r += 1
        
        return maxi
