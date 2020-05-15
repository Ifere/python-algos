# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
#         def check(root, t):
#             if root:
#                 if not root.left and not root.right:
#                     t.append(root.val)
#                 check(root.left, t)
#                 check(root.right, t)
#             return t
#
#         return check(root1, []) == check(root2, [])
