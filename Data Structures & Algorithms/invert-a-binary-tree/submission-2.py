# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = []
        if root:
            q.append(root)

        while q:
            n = q.pop()
            n.right, n.left = n.left, n.right

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return root
        