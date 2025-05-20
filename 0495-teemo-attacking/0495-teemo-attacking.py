class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        output=duration

        for i in range(1,len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1]>=duration:
                output+=duration
            else:
                output+=timeSeries[i]-timeSeries[i-1]
        return output

        