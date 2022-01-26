class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        
        for i in strs:
            
            li = list(i)
            
            li.sort()
            
            x = ''.join(li)
            
            if( x in anagrams.keys()):
                anagrams[x].append(i)
            else:
                anagrams[x] = [i]
                
        res = []
        
        for i in anagrams.keys():
            res.append(anagrams[i])
            
        return res
