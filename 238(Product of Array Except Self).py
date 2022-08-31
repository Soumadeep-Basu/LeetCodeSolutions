class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        FrontMul = []
        F_Mul = 1
        for i in range(len(nums)):
           
            if i==0:
                FrontMul.append(F_Mul)
            else:
                F_Mul *= nums[i-1]
                FrontMul.append(F_Mul)
            
                
            
        RevMul = []
        R_Mul = 1
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                RevMul.append(R_Mul)
            else:
                R_Mul *= nums[i+1]
                RevMul.append(R_Mul)
                
        RevMul.reverse()
        print(FrontMul, RevMul)
        
        
        Answer = []
        
        for i in range(len(nums)):
            Answer.append(FrontMul[i] * RevMul[i])
            
        return Answer
            
            
            
           

            
