class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        
        
        order_left = [0]*len(security)
        
        order_right = [0]*len(security)
        
        
        
        ans = []
        
        for i in range(len(security)):
            if(i == 0):
                order_left[i] = 0
                
            else:
                
                if(security[i] <= security[i-1]):
                    order_left[i] = 1 + order_left[i-1]
                
                
        for j in range(len(security)-1,-1,-1):
            if(j == len(security)-1):
                order_right[j] = 0
                
            else:
                
                if(security[j] <= security[j+1]):
                    order_right[j] = 1 + order_right[j+1]
                    
                    
        for i in range(len(security)):
            
            if(order_left[i] >= time and order_right[i] >= time):
                ans.append(i)
                
                
        return ans
        
                
            
        
