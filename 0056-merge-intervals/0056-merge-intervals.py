class Solution(object):
    def merge(self, intervals):
        
        ans=[]
        print(intervals)
        
        for interval in sorted(intervals,key=lambda interval:interval[0]):

            if ans and interval[0]<=ans[-1][-1]:
                ans[-1][-1]=max(interval[-1],ans[-1][-1])
            else:
                ans.append(interval)
        return ans

        