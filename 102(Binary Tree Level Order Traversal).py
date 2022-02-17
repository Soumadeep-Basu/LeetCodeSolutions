# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        global result
        result = []
        
        def p(l):
            global result
            x = []
            y = []
            for i in l:
                
                if(i.left!=None):
                    x.append(i.left.val)
                    y.append(i.left)
                if(i.right!=None):
                    x.append(i.right.val)
                    y.append(i.right)
            if(len(x)==0):
                return
            else:
                result.append(x)
                
                p(y)
            
        if(root!=None):
            
            result.append([root.val])
            
            y = [root]
            
            p(y)
            
            return result
            
            
        
            
            
            
            
        
