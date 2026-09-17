class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #min day to buy 

        res = 0
        lowest = prices[0]

        for price in prices:
            lowest = min(price, lowest)
            res = max(res, price - lowest)
        return res