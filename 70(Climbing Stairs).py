class Solution:
    global dp 
    dp = {}
    def climbStairs(self, n: int) -> int:
        global dp
        global count
        count = 0
        def laststep(n):
            global count
            if(n==1 or n==0 or n < 0):
                return 1
            else:
                if n in dp.keys():
                    count =  dp[n]
                    return count
                else:
                    
                    dp[n] =  laststep(n-1)+laststep(n-2)
                    return dp[n]
               
     
        
        a = laststep(n)
        
        return a
