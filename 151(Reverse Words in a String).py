class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        ans = []
        
        prev_word = []
        
        index = len(s)
        
        for i in range(index-1, -1, -1):
            if s[i] == ' ':
                if(len(prev_word)!=0):
                    
                    prev_word.reverse()
                    ans.append(''.join(prev_word))
                    prev_word.clear()
                    
            else:
                
                prev_word.append(s[i])
                
          
        if(s[0]!=" "):
            prev_word.reverse()
            ans.append(''.join(prev_word))
                    
                
                
                    
            
        return ' '.join(ans)
