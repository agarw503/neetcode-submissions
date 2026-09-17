class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp, maxp = max(prices), 0
        for p in prices:
            if p < minp:            # p is already the price — don't index into prices
                minp = p
            else:
                maxp = max(maxp, p - minp)
        return maxp