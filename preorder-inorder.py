
# Construct Binary Free from Preorder and Inorder Traversal - leetcode

# Use Preorder list as a list of midpoints
# Midpoints are used as positions to split the inorder list into 2 halfs - left side of list will be all numbers in the left of the tree, right side will be all values in the right side of tree
# Recursively half the list until 1 or no values are left - this will be the bottom of the tree. Return the bottom level treeNode which will be used to build the tree from the bottom up - RECURSIVELY.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):

    print(preorder, inorder)

    if len(inorder) == 0:
        return None

    if(len(inorder) == 1):
        return TreeNode(inorder[0])

    mid = inorder.index(preorder[0])

    return TreeNode(inorder[mid], buildTree(preorder[1:mid], inorder[0:mid]), buildTree(preorder[mid+1:], inorder[mid+1:]))


# Print the Tree
node = buildTree([1, 2, 3], [3, 2, 1])

res = []


def printTree(root):

    if root == None:
        res.append(None)
        return

    adj = [root.left, root.right]

    res.append(root.val)

    for i in adj:
        printTree(i)


printTree(node)

print(res)
