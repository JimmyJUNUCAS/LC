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

def flatten(root):
    while(root!=None):
        if root.left != None:
            most_right = root.left
            while most_right.right != None:
                most_right = most_right.right
            most_right.right = root.right
            root.right = root.left
            root.left = None
        root = root.right
    return
print(flatten(l1_1))

# 完全二叉树的节点个数
def countNode(root):
    return 1 + countNode(root.right) +countNode(root.left) if root else 0
print(countNode(l1_1))

def compute_depth(node):
    d = 0
    while node.left:
        node = node.left
        d += 1
    return d
def exist(idx,d,node):
    left,right = 0,2**d-1
    for _ in range(d):
        pivot = left + (right - left)//2
        if idx <= pivot:
            node = node.left
            right = pivot
        else:
            node = node.right
            left = pivot + 1
    return node is not None

def countNode(root):
    if not root : return 0
    d = compute_depth(root)
    if d == 0 : return 1
    left,right = 1,2**d-1
    while left <= right:
        pivot = left + (right - left)//2
        if exist(pivot,d,root):
            left = pivot + 1
        else:
            right = pivot - 1
    return (2**d - 1)+left
print(countNode(l1_1))

def kthSmallest(root,k):
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    return inorder(root)[k-1]
print(kthSmallest(l1_1,2))

def kthSmallest(root,k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right
print(kthSmallest(l1_1,5))