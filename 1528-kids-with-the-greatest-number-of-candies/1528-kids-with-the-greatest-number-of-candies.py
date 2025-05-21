class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_val=max(candies)
        sol=[]

        for i in candies:
            if i+extraCandies>=max_val:
                sol.append(True)
            else:
                sol.append(False)
        return sol
        