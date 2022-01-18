class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        wordmap = {}
        
        word = s.split()
  
        
        print(word)
        
        if(len(word)!=len(pattern)):
            return False
        
        try:
            
            for i in range(len(pattern)):
                if(pattern[i] in wordmap.keys()):
                    if(wordmap[pattern[i]]!=word[i]):
                        return False
                else:
                    for j in range(0,i):
                        if(word[j] == word[i]):
                            return False
                    wordmap[pattern[i]]=word[i]
                    
        except:
            return False
        
        
        
        
        
        return True
                        
                
                    
            
            
        
