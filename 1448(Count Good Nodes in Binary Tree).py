# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def goodNodes(self, root: TreeNode) -> int:
        
       
        self.count = 0
        
        
        def GetGoodNode(self, Node, PrevVal):
            if Node == root:
                self.count+=1
                GetGoodNode(self, Node.left, Node.val)
                GetGoodNode(self, Node.right, Node.val)
            elif(Node == None):
                return
            else:
                if(Node.val >= PrevVal):
                    self.count+=1
                    GetGoodNode(self, Node.left, Node.val)
                    GetGoodNode(self, Node.right, Node.val)
                else:
                    GetGoodNode(self, Node.left, PrevVal)
                    GetGoodNode(self, Node.right, PrevVal)
                    
                
         
            return
        
 
        if(root == None):
            return 0
        elif(root.left == None and root.right == None):
            return 1
        else:    
            GetGoodNode(self, root, root.val)
            
        return self.count
