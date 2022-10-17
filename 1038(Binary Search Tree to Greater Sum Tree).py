# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
       
    
        self.MaxArr = []
        
        
        self.mem = {}


        def Populate(Node):

            if( not Node):
                return
            else:

                Populate(Node.left)
                self.MaxArr.append(Node.val)
                Populate(Node.right)
                
                
                
        def ans(Node):
            
            
            if(not Node):
                return
            else:
                
                ans(Node.left)
                Node.val = self.mem[Node.val]
                ans(Node.right)

                
            
            


        Populate(root)

        
        Sum = 0

        for i in range(len(self.MaxArr)-1 , -1, -1):
            
            Sum+= self.MaxArr[i]
            self.mem[self.MaxArr[i]] = Sum
            
            
        ans(root)
        
        
        return root

            
            
        
            
            








