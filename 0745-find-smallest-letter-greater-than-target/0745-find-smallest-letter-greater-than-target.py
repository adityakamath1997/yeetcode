class Solution(object):
    def nextGreatestLetter(self, letters, target):
        min_diff=27
        L=""

        for letter in letters:
            diff=ord(letter)-ord(target)
            if diff!=0 and 0<diff<min_diff:
                L=letter
                min_diff=diff
        
        if L=="":
            return letters[0]
        return L


        