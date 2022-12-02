# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        if root is None:
            return []
        
        left_path = self.binaryTreePaths(root.left)
        right_path = self.binaryTreePaths(root.right)
        
        for path in left_path:
            result.append(str(root.val) + '->' + str(path))
            
        for path in right_path:
            result.append(str(root.val) + '->' + str(path))
            
        if root.left is None and root.right is None:
            result.append(str(root.val))
            
        return result