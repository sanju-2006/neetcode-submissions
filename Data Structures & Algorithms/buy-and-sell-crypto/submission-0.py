class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest=float('inf')
        best=0
        for price in prices:
            cheapest=min(cheapest,price)
            best=max(best,price-cheapest)
        return best