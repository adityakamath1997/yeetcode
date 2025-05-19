class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price=0
        l,r=0,1

        while r<len(prices):
            max_price=max(max_price,prices[r]-prices[l])
            if prices[l]>=prices[r]:
                l=r
                r+=1
            else:
                r+=1
        return max_price
        

