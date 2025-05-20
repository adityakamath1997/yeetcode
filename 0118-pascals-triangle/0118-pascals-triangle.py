class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[1]
        output=[arr]
        for i in range(1,numRows):
            ans=[]
            arr=[0]+arr+[0]
            for i in range(1,len(arr)):
                s=int(arr[i])+int(arr[i-1])
                ans.append(int(s))
            arr=ans
            output.append(ans)
        return output
        