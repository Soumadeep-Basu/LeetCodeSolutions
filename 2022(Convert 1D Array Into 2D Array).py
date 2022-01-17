class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        
        index = 0
        
        
        if(m*n != len(original)):
            return matrix
    
        try:
            
            for i in range(m):
                row = []
                for j in range(n):
                    row.append(original[index])
                    index = index + 1
                matrix.append(row)
            return matrix
        except:
            martix = []
            return matrix
                
