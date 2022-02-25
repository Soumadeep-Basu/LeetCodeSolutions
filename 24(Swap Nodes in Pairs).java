/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {

       
        //Base case 1
        if(head==null){
            return head;
        }
        //Base case 2
        else if(head.next == null){
            return head;
        }
        else {
        //Create a reference for head to point to the start after iteration ends
        ListNode T = new ListNode(head.val, head.next);
        T = head;
            
        //Create 
        ListNode prev_pointer = new ListNode(head.val, head.next);
        prev_pointer = head;
            
        head = head.next;
            
            //Iterate through the linked list
            while(head!=null){
                int temp = head.val;
                head.val = prev_pointer.val;
                prev_pointer.val = temp;
                 
                //break point
                if(head.next==null){
                    break;
                }
                
                prev_pointer = head.next;
                head = prev_pointer.next;
                
                
                
            }
        
        
            head = T;
            
        }
        
        
        
        
        
        
            
            
    
    return head;
        
    }
}
