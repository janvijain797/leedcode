class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        l_sum = 0 
        r_sum = 0
        max_sum = 0 
        for i in range(0,k):
            l_sum = l_sum + cardPoints[i]
            max_sum = l_sum
            r = len(cardPoints)-1 
        for i in range(k-1 ,-1, -1 ):
            l_sum= l_sum -cardPoints[i]
            r_sum =r_sum + cardPoints[r]
            r = r-1 
            max_sum= max(max_sum, l_sum + r_sum)
        return max_sum
