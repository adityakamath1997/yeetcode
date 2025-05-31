class Solution(object):
    def nextGreatestLetter(self, letters, target):
        L,R=0,len(letters)-1

        if target>=letters[-1] or len(letters)==0:
            return letters[0]

        while L<=R:
            mid=(L+R)//2

            if target>=letters[mid]:
                L=mid+1
            else:
                R=mid-1
        return letters[L]
        

