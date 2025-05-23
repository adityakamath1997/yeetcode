class Solution(object):
    def distributeCandies(self, candyType):
        unique=set(candyType)
        return min(len(unique),len(candyType)/2)

        