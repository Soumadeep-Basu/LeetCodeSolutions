
            
            
            
            
        class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        LookUp = {}
        
        Answer = []
        
        for num in nums:
            if num in LookUp:
                LookUp[num]+=1
            else:
                LookUp[num] = 1
        
                
        for i in range(k):
            max_c = 0
            max_ele = 0
            
            for k in LookUp.keys():
                if LookUp[k] > max_c:
                    max_c = LookUp[k]
                    max_ele = k
            
            Answer.append(max_ele)
            
            LookUp.pop(max_ele)
            
        return Answer
                
                
        
        
