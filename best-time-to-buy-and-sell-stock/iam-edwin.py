from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        startPrice = prices[0]
        maxPrice = prices[0]

        for price in prices[1:]:
            if price < startPrice:
                maxProfit = max(maxProfit, maxPrice - startPrice)
                startPrice = price
                maxPrice = price
            else:
                maxPrice = max(maxPrice, price)

        return max(maxProfit, maxPrice - startPrice)
