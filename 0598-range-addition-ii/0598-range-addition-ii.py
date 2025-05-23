class Solution(object):
    def maxCount(self, m, n, ops):
        min_i=m
        min_j=n

        for op in ops:
                min_i,min_j=min(min_i,op[0]),min(min_j,op[1])
        return min_i*min_j
        