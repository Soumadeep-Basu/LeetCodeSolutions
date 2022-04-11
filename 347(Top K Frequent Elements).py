class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #define dict to store the occurances of each word
        occurance = {}
        
        #count the number of occurances
        for i in nums:
            if i in occurance:
                occurance[i]+= 1
            else:
                occurance[i] = 1
                
        
        #sort the dict, and rearrange elements
        occurance = sorted(occurance.items(), key = lambda x : x[1] , reverse = True)
        
        #define the result
        resultList = []
        
        #Append first k elements
        for i in range(k):
            resultList.append(occurance[i][0])
            
        return resultList
            
            
            
            
        
