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

def hasPathSum(root,sum):
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return hasPathSum(root.left,sum) or hasPathSum(root.right,sum)
print(hasPathSum(l1_1,8))

def hasPathSum(root,sum):
    if not root : return False
    de = [(root,sum-root.val),]
    while de:
        node,curr_sum = de.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            de.append((node.right,curr_sum-node.right.val))
        if node.left:
            de.append((node.left,curr_sum-node.left.val))
    return False
print(hasPathSum(l1_1,8))

# 二叉树最大路径
# def maxPathSum(root):
#     def max_gain(node):
#         nonlocal max_sum
#         if not node:
#             return 0
#         left_gain = max(max_gain(node.left),0)
#         right_gain = max(max_gain(node.right),0)
#         price_newpath = node.val + max(left_gain,right_gain)
#     max_sum = float('-inf')
#     max_gain(root)
#     return max_sum
# print(maxPathSum(l1_1))

# 二叉树展开为链表
def flatten(root):
    def helper(root):
        if root == None :return
        helper(root.left)
        helper(root.right)
        if root.left != None:
            pre = root.left
            while pre.right:pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None
        root = root.right
    helper(root)
print(flatten(l1_1))

# def flatten(root):
#     while root !=


