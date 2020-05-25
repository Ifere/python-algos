"""
    serialize:
        preorder_search
        inorder_Search
        
        
        return [preorder, inorder]

    deserialize:
    root = 1
    left_subtree = [2]
    right_subtree = [4,3,5]
    
    inorder = [2]
    root = 2
    left = [], None
    right =[], None
    
    inorder = [4,3,5]
    root = [3]
    left = [4]
    right = [5]

    ...
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.right.left = TreeNode(5)
a.right.right = TreeNode(5)



preorder_mapping = {}
index = [0]

def preorderAndInorder(root):
    pre_result = []
    in_result = []

    def makeNewTree(root):
        if root:
            preorder_mapping[index[0]] = root.val
            root.val = index[0]

            index[0] += 1

            makeNewTree(root.left)
            makeNewTree(root.right)

    makeNewTree(root)

    def helper(current):

        pre_result.append(current.val)

        if current.left:
            helper(current.left)

        in_result.append(current.val)

        if current.right:
            helper(current.right)

    helper(root)

    return pre_result, in_result


def serialize(root):
    return preorderAndInorder(root)


def deserialize(preorder, inorder):

    preorder_iter = iter(preorder)

    def helper(pre_iter, in_list):

        if not in_list:
            return None

        node_val = next(pre_iter)

        index = in_list.index(node_val)

        node = TreeNode(preorder_mapping[node_val])

        left_subtree = in_list[:index]
        right_subtree = in_list[index+1:]

        node.left = helper(pre_iter, left_subtree)
        node.right = helper(pre_iter, right_subtree)


        return node

    return helper(preorder_iter, inorder)


result = serialize(a)

b = deserialize(result[0], result[1])

def print_tree(root):

    if root:

        print_tree(root.left)

        print(root.val)

        print_tree(root.right)


print(print_tree(b))


# test = [1,2,1, 3, 1]
# last_start = defaultdict(int)
#
# next_index = test.index(1, last_start[1])
# print(next_index)
#
# last_start[1] = next_index + 1
# next_index = test.index(1, last_start[1])
# print(next_index)
#
# last_start[1] = next_index + 1
# next_index = test.index(1, last_start[1])
# print(next_index)
#



"""
preorder = [1,2,1,4,5]

pre_mapping = {1:0, 2:1, 1:2
inorder = [2,1,4,3,5]
"""



"""

            1
        /
    

"""
