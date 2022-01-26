class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        

        
        prof = 0
        j = 0
        profit_worker = 0
        
        for i in range(len(difficulty)):
            difficulty[i] = [difficulty[i], profit[i]]
            
        difficulty.sort()
        
        
                 
        for i in sorted(worker):
            
            
            
            while(j<len(difficulty) and difficulty[j][0]<=i):
                profit_worker = max(profit_worker, difficulty[j][1])
                j+=1
            prof+=profit_worker
            

        return prof
            
        
