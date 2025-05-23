class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)
        max_candies=n/2
        coll=set()
        for i in candyType:
            coll.add(i)

        return min(max_candies,len(coll))

        