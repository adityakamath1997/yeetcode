class Solution(object):
    def merge(self, intervals):
        
        ans=[]
        intervals=sorted(intervals,key=lambda interval:interval[0])
        print(intervals)
        
        for interval in intervals:

            if ans and interval[0]<=ans[-1][-1]:
                ans[-1][-1]=max(interval[-1],ans[-1][-1])
            else:
                ans.append(interval)
        return ans

        