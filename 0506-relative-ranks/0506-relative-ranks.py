class Solution(object):
    def findRelativeRanks(self, score):
        sorted_scores=sorted(score,reverse=True)
        ranks={}
        ans=[]
        for i in range(len(sorted_scores)):
            ranks[sorted_scores[i]]=str(i+1)

        
        
        ranks[sorted_scores[0]]="Gold Medal"
        if len(score)>1:
            ranks[sorted_scores[1]]="Silver Medal"
        if len(score)>2:
            ranks[sorted_scores[2]]="Bronze Medal"

        print(ranks)

        for s in score:
            ans.append(ranks[s])

        return ans

        

        