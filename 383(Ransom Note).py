class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        visited=[]
        
        note = list(ransomNote)
        mag = list(magazine)
        
        
        for i in note:
            if(mag.count(i)==0):
                return False
            else:
                x = mag.index(i)
                mag[x] = "0"
                
        return True
