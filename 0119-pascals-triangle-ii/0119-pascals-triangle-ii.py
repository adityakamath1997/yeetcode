class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output=list()

        def factorial(n):
            if n<=1:
                return 1
            else:
                return n*factorial(n-1)
        
        for i in range(0,rowIndex+1):
            output.append(int(factorial(rowIndex)/(factorial(i)*factorial(rowIndex-i))))
        return output
            
