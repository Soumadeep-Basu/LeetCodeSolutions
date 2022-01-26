# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = []
        l2 = []
        
        def traverse(root, l):
            if(root==None):
                return l
            else:
                l.append(root.val)
                if(root.left!=None):
                    l = traverse(root.left, l)
                if(root.right!=None):
                    l = traverse(root.right, l)
            return l
        
        l1 = traverse(root1,l1)
        l2 = traverse(root2,l2)
        
        l1.sort()
        l2.sort()
        
        i,j = 0,0
        res=[]
       
        l1 = l1+l2
        l1.sort()
        
        
        return l1
        
        
        

                    
