class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Res = 0
        Prev = 0
        L = 0
        R = 1

        while R < len(prices):
            if prices[R] - prices[L] > Prev:#meaning we found higher profit
                Res = max(Res, prices[R] - prices[L])
                prev = prices[R] - prices[L] 
            else:
                L = R
            R += 1
        return Res

