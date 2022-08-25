# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        stack, r, poped = [[root, 0]], [], False
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                poped = True

                if top[0].right:
                    stack.append([top[0].right, 0])
                    poped = False

            elif top[0].left and not poped:
                stack.append([top[0].left, 0])
            else:
                r.append(top[0].val)
                top[1] = 1
        return r
