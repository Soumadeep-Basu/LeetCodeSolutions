class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        substring = list(s)
        
        string = list(t)
        i,j = 0,0
        
        while(i<len(substring) and j<len(string)):
            
            if(substring[i] == string[j]):
                i+=1
                j+=1
            elif(substring[i]!=string[j]):
                j+=1
           
            
        if(i==len(substring)):
            return True
        else:
            return False
