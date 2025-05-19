class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price=0
        l=0
        r=1

        while r<=len(prices)-1:
            max_price=max(max_price,(prices[r]-prices[l]))
            if prices[r]<=prices[l]:
                l=r
                r+=1
            else:
                r+=1
            print(l,r)
            

        return max_price

