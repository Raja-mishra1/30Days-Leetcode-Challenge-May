class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        trust_score = [ 0 for _ in range(N+1) ]
        
        for p1, p2 in trust:
            trust_score[p1] -=1
            trust_score[p2] +=1
            
            
        
        for person in range(1, N+1):
            if trust_score[person] == N-1:
                return person
        
        return -1