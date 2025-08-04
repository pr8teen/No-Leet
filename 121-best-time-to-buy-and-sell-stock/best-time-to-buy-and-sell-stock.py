class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            curr_p = prices[i] - min_p
            if curr_p > profit:
                profit = curr_p
            min_p = min(min_p,prices[i])
        return profit