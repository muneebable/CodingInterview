class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_till_now= prices[0]
        for i in prices[1:]:
            if min_till_now>i:
                min_till_now=i
            else:
                profit= max(profit, (i-min_till_now))
        return(profit)
