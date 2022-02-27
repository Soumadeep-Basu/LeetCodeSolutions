# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def sort_stack(self,X):
        
        index = len(X) - 1
        while(index > 0):
            
            cur = X[index]
            prev = X[index-1]
            
            if(cur.val > prev.val):
                cur, val = val , cur
            index = index -1 
                
        return X
            
        
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        X = []
        
        start_index = head
        
        while (head!=None):
            
            if(len(X)==0):
                X.append(head)
                X = self.sort_stack(X)
                head = head.next
            else:
                i = len(X)-1
                node = X[i]
                if node.val < head.val:
                    while X[len(X)-1].val < head.val:
                        X[len(X)-1].val = head.val
                        X.pop(len(X)-1)
                        if len(X)==0:
                            break
                    X.append(head)
                    X = self.sort_stack(X)
                    head = head.next
                else:
                    X.append(head)
                    head = head.next
                  
            
            
        for i in X:
            i.val = 0
                                 
                                 
        head = start_index
        
        res = []
        
        while(head!= None):
            res.append(head.val)
            head = head.next
            
        return res
                        
                                 
                                 

