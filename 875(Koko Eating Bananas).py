class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def ispossible(pile, h, n):
            
            count = 0
            
            for i in range(len(pile)):
                
                x = math.ceil(pile[i]/n)
                
                count = count + int(x)
            
            if(count<=h):
                
                
                return True
            else:
                
                return False
                
            
        min_eats = 1
        max_eats = max(piles)
        
        while(min_eats < max_eats):
            eats= (min_eats + max_eats) //2
            
            if(ispossible(piles,h,eats)):
                max_eats = eats
            else:
                min_eats = eats + 1
                
        return min_eats
            
        

        
