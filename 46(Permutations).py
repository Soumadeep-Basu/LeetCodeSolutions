class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def createPermutations( output,nums, index):
            
            if(index == len(nums)):
                output.append(nums[:])
            else:
                for i in range(index, len(nums)):
                    nums[i], nums[index] = nums[index], nums[i]
                
                    output = createPermutations(output, nums, index+1)
                    
                    nums[i], nums[index] = nums[index], nums[i]
                
                   
                    
            return output
        
        index = 0
        output = []
        
        res = createPermutations(output, nums, index)
        
        return res
        
        
            
        
