class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                print(cur, res)
                res += prices[i-1] - cur
                cur = prices[i]
        if len(prices) > 1 and prices[-1] >= prices[-2]:
            res += prices[-1] - cur


        return res



        