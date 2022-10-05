class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mem_table = {}
        
        scaleFactor = (10**9) + 7
        
        def find_steps(currSum, numDice):
            
            if(numDice<0 or (numDice==0 and currSum!=0) or currSum<0):
                return 0
            elif(currSum==0 and numDice==0):
                return 1
            else:
                if (currSum,numDice) in mem_table:
                    return mem_table[(currSum,numDice)]
                else:
                    s=0
                    for i in range(1,k+1,1):
                        s = (s + find_steps(currSum-i,numDice-1))%scaleFactor
                        
                    mem_table[(currSum, numDice)] = s 
                        
                    
                    return mem_table[(currSum, numDice)]
            
        
        ans = find_steps(target,n)
       
        
        
            
        
        return ans
        
