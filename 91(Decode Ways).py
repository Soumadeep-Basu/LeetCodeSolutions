class Solution:
    def numDecodings(self, s: str) -> int:
        
        self.count = 0
        
        self.memo = {}
        
  
        
        def count_ways(s, index):
            if (index == len(s)-1):
                return 1
            else:
                i = index + 1
                j = index + 2
                if(j <= len(s) -1 and int(s[i]+s[j])<=26 and s[i]!="0"):
                    
                    if (i,j) in self.memo:
                        count = self.memo[(i,j)]
                    else:
                        
                        self.memo[(i,j)] = count_ways(s,i) + count_ways(s,j)
                        count = self.memo[(i,j)]
                elif(i<= len(s)-1 and s[i]!="0"):
                    if (i,i) in self.memo:
                        count = self.memo[(i,i)]
                    else:
                        self.memo[(i,i)] = count_ways(s,i)
                        count = self.memo[(i,i)]
                else: 
                    return 0
                 
                        
            return count
        
        if s[0]=="0":
            return 0
        
        count = count_ways(s, -1)
        
       
        
        return(count)
            
