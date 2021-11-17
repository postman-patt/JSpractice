# INORDER TRAVERSIAL - provides the correct order


def isValidBST(root):

    inorder = []

    def inorder_traversial(r, inorder):
        if r:
            inorder_traversial(r.left, inorder)
            inorder.append(r.val)
            inorder_traversial(r.right, inorder)

    inorder_traversial(root, inorder)

    return sorted(inorder) == inorder and len(inorder) == len(set(inorder))
