class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        down = [1]*len(nums)
        
        up = [1]*len(nums)
        
        
        
        for i in range(len(nums)):
            
            if(i == 0):
                continue
            else:
                if(nums[i] < nums[i-1]):
                    down[i] =  up[i-1] + 1
                    up[i] = up[i-1]
                elif(nums[i] > nums[i-1]):
                    down[i] = down[i-1]
                    up[i] = down[i-1] + 1
                else:
                    down[i] = down[i-1]
                    up[i] = up[i-1]
                    
                    
        print(down, up)
                    
        return max(down[len(nums)-1] , up[len(nums)-1])
        
