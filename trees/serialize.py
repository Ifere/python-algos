class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.right.left = TreeNode(4)
a.right.right = TreeNode(5)


"""
serialize:
preorder search
inorder search

return [preorder, inorder]
"""


def serialize(root):

    pre, inorder = preandIn(root)
    print(pre, inorder)

    pass


def preandIn(root):
    pre = []
    inorder = []

    def helper(current):
        pre.append(current.val)

        if current.left:
            helper(current.left)

        inorder.append(current.val)

        if current.right:
            helper(current.right)

    helper(root)

    return pre, inorder



"""
"""


def deserialize(preorder, inorder):
        preorder_iter = iter(preorder)

        def helper(pre_iter,in_list):

            node_val = next(pre_iter)

            index = in_list.index(node_val)

            node = TreeNode(node_val)

            left_subtree = in_list[:index]
            right_subtree = in_list[index+1:]

            node.left = helper(pre_iter, left_subtree)
            node.right = helper(pre_iter, right_subtree)

            return node


def print_tree(root):

    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


