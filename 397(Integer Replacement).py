class Solution:
    
    
    def step_count(self,n,steps):
        if(n <=1 ):
            return steps
        elif(n % 2 == 0):
            
            steps = self.step_count(n//2, steps)
            steps = steps + 1
            return steps
        else:
            if n in self.m.keys():
                steps = steps + self.m[n]
                return steps
            else:
                
                steps = min(self.step_count(n+1, steps), self.step_count(n-1,steps))
                steps = steps + 1
                self.m[n] = steps
                return steps
                
         
                
    def integerReplacement(self, n: int) -> int:
        self.m = {} 
        
        steps = 0
        
        steps = self.step_count(n, steps)
        
        return steps
        
