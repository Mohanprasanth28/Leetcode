# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaf(root1) == self.leaf(root2)
    
    def leaf(self,root):
        arr = []
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:  
                arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return arr
        