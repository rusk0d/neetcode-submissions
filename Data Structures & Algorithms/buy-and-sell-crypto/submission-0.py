class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0

        for price in prices:
            if price < lowest:           # is this a new lowest price?
                lowest = price
            if (price - lowest) > best:
                best = (price - lowest)

        return best