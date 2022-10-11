class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        mem_table = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
       
        for i in range(1,len(text1)+1,1):
            for j in range(1,len(text2)+1,1):
                
                if(text2[j-1] == text1[i-1]):
                    mem_table[i][j] = 1 + mem_table[i-1][j-1]
                    
                else:
                    mem_table[i][j] = max(mem_table[i-1][j], mem_table[i][j-1])
                    
                    
                    
        return mem_table[len(text1)][len(text2)]
