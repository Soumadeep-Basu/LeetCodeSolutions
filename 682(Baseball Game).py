class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        record = []
        
        for i in range(len(ops)):
            if(ops[i]=="C"):
                record.pop()
            elif(ops[i]=="D"):
                record.append(2*int(record[len(record)-1]))
            elif(ops[i]=="+"):
                
                record.append(int(record[len(record)-1]) + int(record[len(record)-2]))
            else:
                record.append(ops[i])
                
        score = 0
  
        for i in record:
                score = score + int(i)
            
        return score
