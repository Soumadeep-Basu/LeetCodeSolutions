class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        max_list = [0]*len(nums)
        
        
        for i in range( len(nums)):
            
            if(i == 0):
                
                max_list[i] = nums[i]
                
            elif(i == 1):
                max_list[i] = max(nums[i], max_list[i-1])
                
            else:
                
                max_list[i] = max(nums[i] + max_list[i-2], max_list[i-1])
                
                
        return max_list[len(max_list)-1]
