class Solution(object):
    def lengthOfLIS(self, nums):
        
        maxlength = [1]*len(nums)
        
        maxs = 0
        
        flag =0
        
        
        
        print(maxlength)
        
        for i in range(len(nums)):
            temp = 1
            flag = 0
            for j in range(0,i):
                if(nums[j] < nums[i]):
                    if(temp <=maxlength[j]):
                        temp = maxlength[j]
                        flag =1          
            if(flag==1):     
                maxlength[i] = 1 + temp
        
        
           
           
        return max(maxlength)
                    
                    
                    
                
                
                
                    
                    
                
                
                
        
        
        
