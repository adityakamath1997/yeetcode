class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        output=0

        for i in range(len(timeSeries)):
            if i==len(timeSeries)-1:
                output+=duration
            else:
                if timeSeries[i+1]-timeSeries[i]>=duration:
                    output+=duration
                else:
                    output+=timeSeries[i+1]-timeSeries[i]
        return output

        