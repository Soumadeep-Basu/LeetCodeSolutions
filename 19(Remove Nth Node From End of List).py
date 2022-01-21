# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        
        if(head.next==None):
            head=head.next
            return head
        
        temp = head
        
        
        while(temp.next!=None):
            count+=1
            temp = temp.next
        
        count+=1
        
        temp = head
        
        for i in range(count-n):
            temp = temp.next

        
        prev = head
        
        while(prev.next!=temp and prev!=temp):
            prev=prev.next
        if(prev==temp):
            head=temp.next
        else:
            prev.next = temp.next
        
        return head
            
       
        
        
        
