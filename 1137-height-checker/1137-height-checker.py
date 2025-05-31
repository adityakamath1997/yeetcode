class Solution(object):
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        ct=0
        for h1,h2 in zip(heights,sorted_heights):
            if h1!=h2:
                ct+=1
        return ct
        