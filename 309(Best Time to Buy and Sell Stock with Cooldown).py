class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.mem_table = {}
        
        
        
        def MaxPro( index ):
            
            if index[0] >= len(prices):
                return 0
            elif index in self.mem_table:
                return self.mem_table[index]
            
            else:
                
                if(index[1] == -1):
                    
                    buy = MaxPro((index[0] + 1, 1)) - prices[index[0]]
                    cooldown = MaxPro((index[0] + 1, -1))
                    self.mem_table[index] = max(buy, cooldown)
                    
                elif(index[1] == 1):
                    
                    sell = MaxPro((index[0] + 2, -1)) + prices[index[0]]
                    cooldown = MaxPro((index[0] + 1, 1))
                    self.mem_table[index] = max(sell, cooldown)
                    
            
            return self.mem_table[index]
                    
                    
        
        MaxPro((0,-1))
        
        
        return self.mem_table[(0,-1)]
                    
                
                
        

            
            
                
        
                    
        
        
        
        
        
