class Solution:
    def maxProfit(self, prices):
        m = len(prices)
        minPrice = float("inf")
        maxPrice = 0
        for price in prices:
            minPrice = min(minPrice,price)
            maxPrice = max(maxPrice, price-minPrice)
        return maxPrice