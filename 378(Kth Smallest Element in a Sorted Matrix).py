class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        
        def findCount(m):
            
            count = 0
            
            for i in range(len(matrix)):
                
                c = bisect_right(matrix[i], m)
                
                count+= c
                
            return count
        
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        
       
        
        
        while(l < r):
            mid = (l+r) // 2
            
            if(findCount(mid) < k):
                l = mid + 1
            else:
                r = mid
                
        return l
        
        
                
                
        
        
        
