class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        
        temp = list(s)
            
        subsequence = list(p)
        
        def issubsequence(s, p):
            
            i = 0
            j = 0
            
            
            while(j<len(s)):
               
                if(s[j] == p[i]):
                    i+=1
                    j+=1
                    if(i>=len(p)):
                        return True
                else:
                    j+=1
                    
            return False
        
        
        
        
        
        prev = 0
        top = len(removable)
        
        while(prev<top):
            
            string = list(s)
            index = (prev+top) // 2
            j = 0
            
            while(j<=index):
                
                string
                x = removable[j]
                string[x]="0"
                j+=1
                
            if(issubsequence(string,subsequence)):
                prev = index + 1
                
            else:
                top = index
                
        temp[removable[0]]="0"
        print(string,temp)
        if(issubsequence(temp, subsequence) and int(prev)==0):
            return 1
        else:
            
            return int(top)
    
            
                         
            
            
            

            
        
