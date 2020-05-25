def check(left: TreeNode, right: TreeNode):
    if left == None and right == None:
        return True
    elif left != None and right != None:
        return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
    else:
        return False


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            return check(root.left, root.right)

