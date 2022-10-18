class Solution:
    def maximumSwap(self, num: int) -> int:
        
        
        
        
        num = list(str(num))
        
           
        refArr = [0]*len(num)
        
        for i in range(len(num)):
            refArr[i] = num[i]
        
        refArr.sort(reverse=True)
        
        print(refArr,num)
        
        index = []
        
       
        for i in range(len(num)):
            
            if(num[i]!=refArr[i]):
                
                for k in range(i, len(num),1):
                    if num[k] == refArr[i]:
                        index.append([k,i])
                        
                break
                
                
        
                

        if(len(index)==0):
            return ''.join(num)
        else:
            

            Max = 0

            for i in index:

                num[i[0]],num[i[1]] = num[i[1]],num[i[0]]


                if( int(''.join(num)) > Max):
                    Max = int(''.join(num))

                num[i[0]],num[i[1]] = num[i[1]],num[i[0]]



            return Max
                
            
            
        
       
                    
                    
        
                    
        
        
            
        
