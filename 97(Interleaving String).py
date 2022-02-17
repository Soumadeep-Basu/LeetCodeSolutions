class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
# Recursive Solution
#         def check(i,j):
            
#             if(i == len(s1) and j == len(s2)):
#                 return True
#             else:
                
#                 x,y = False,False
                
#                 if( i < len(s1) and s3[i+j]==s1[i]):
#                         x = check(i+1, j )
                        
                    
#                 if ( j < len(s2) and s3[i+j]==s2[j]):
#                         y = check(i, j+1)
                        
                    
#                 return (x or y)
            
            
        if(len(s1) + len(s2)!= len(s3)):
            return False
        if(s1 == "" or s2 == ""):
            return s1==s3 or s2==s3
     
        
        dp = [[False for i in range(len(s2) +1)] for j in range(len(s1) + 1)]
        
        dp[len(s1)][len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                
                if(i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]):
                    dp[i][j] = True
                if(j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]):
                    dp[i][j] = True
                    
        return dp[0][0]
                
                
                
                
                
        
        
        
