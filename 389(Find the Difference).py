class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        a = list(s)
        
        b = list(t)
        
        a.sort()
        b.sort()
        
        for i in range(len(b)):
            if(i==len(a)):
                return b[i]
            elif(a[i]==b[i]):
                pass
            else:
                return b[i]
