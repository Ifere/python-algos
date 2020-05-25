class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)

"""
def summer(root):
 nodes = []
 agg = 0
 def checkEvery(root, level):
    if root == None:    
        return
    
    nodes.append([root.val,  level])
    checkEvery(node.left, level +1)
    checKEvery(node.right, level+1)
        
for node in nodes:
    agg += node[1]  
        
 
"""

nodes = []
agg = 0



def check(root, level):
    if root is None:
        return
    nodes.append([root.val, level])
    print([root.val, level])
    check(root.left, level + 1)
    check(root.right, level + 1)


def summer(n):
    b = 0

    for node in n:
        b += node[1]
    return b


check(a, 0)
print(summer(nodes))



