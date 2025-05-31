class Solution(object):
    def nextGreatestLetter(self, letters, target):
        min_diff=27
        L,R=0,len(letters)-1

        while L<R:
            mid=(L+R)//2
            if ord(target)<ord(letters[mid]):
                R-=1
            else:
                L+=1
        if ord(letters[R])-ord(target)>0:
            return letters[R]
        return letters[0]


        