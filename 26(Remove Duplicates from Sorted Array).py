class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        currIndex = 0
        nextIndex = currIndex+1
        
        currVal = 0
        
        
        while(currIndex != len(nums) and nextIndex!=len(nums)):
            
            currVal = nums[currIndex]
            
            if(nums[nextIndex]==currVal):
                nextIndex+=1
            else:
                
                currIndex += 1
                nums[currIndex] = nums[nextIndex]
                currVal = nums[nextIndex]
                
        
        return currIndex + 1
