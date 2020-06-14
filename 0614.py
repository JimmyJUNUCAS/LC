class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
l1_1 = TreeNode(1)
l1_2 = TreeNode(2)
l1_3 = TreeNode(3)
l1_4 = TreeNode(4)
l1_5 = TreeNode(5)
l1_6 = TreeNode(6)
l1_7 = TreeNode(7)

l1_1.left = l1_2
l1_1.right = l1_7
l1_2.left = l1_3
l1_2.right = l1_4
l1_4.left = l1_5
l1_4.right = l1_6

def buildTree(inorder,postoder):
    def helper(in_left,in_rihgt):
        if in_left > in_rihgt:
            return None
        val = postoder.pop()
        root = TreeNode(val)
        index = idx_map[val]
        root.right = helper(index+1,in_rihgt)
        root.left = helper(in_left,index-1)
        return root
    idx_map = {val:idx for idx,val in enumerate(inorder)}
    return helper(0,len(inorder)-1)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(buildTree(preorder,inorder))