class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        orig=abs(x)
        s=0
        r=0

        while orig>0:
            r=orig%10
            s=s*10+r
            orig=orig//10
        
        if x<0:
            s=-1*s

        if s<-2**31 or s>(2**31)-1:
            return 0
        
        return s