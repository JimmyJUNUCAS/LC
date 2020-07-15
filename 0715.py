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

