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

def inorderTraversal(root):
    res = []
    def dfs(root):
        if not root: return 0
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    dfs(root)
    return res
print(inorderTraversal(l1_1))

def preorderTraversal(root):
    res = []
    def dfs(root):
        if not root : return 0
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return res
print(preorderTraversal(l1_1))

def postorderTraversal(root):
    res = []
    def dfs(root):
        if not root : return 0
        dfs(root.left)
        dfs(root.right)
        res.append(root.val)
    dfs(root)
    return res
print(postorderTraversal(l1_1))

def inorderTraversal(root):
    res = []
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
    return res
print(inorderTraversal(l1_1))

def preorderTraversal(root):
    res = []
    stack = [root,]
    while stack and root:
        root = stack.pop()
        res.append(root.val)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)
    return res
print(preorderTraversal(l1_1))

def postorderTraversal(root):
    res = []
    stack = [root,]
    while stack and root:
        root = stack.pop()
        res.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return res[::-1]
print(postorderTraversal(l1_1))

def levelOrder(root):
    if not root : return 0
    res = []
    def dfs(index,r):
        if len(res) < index:
            res.append([])
        res[index-1].append(r.val)
        if r.left:
            dfs(index+1,r.left)
        if r.right:
            dfs(index+1,r.right)
    dfs(1,root)
    return res
print(levelOrder(l1_1))

def levelOrder(root):
    if not root : return 0
    res = []
    stack = [root]
    while stack:
        tmp = []
        for _ in range(len(stack)):
            r = stack.pop(0)
            tmp.append(r.val)
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        res.append(tmp)
    return res
print(levelOrder(l1_1))

def levelOrder(root):
    res = []
    stack = [root]
    while stack and root:
        tmp = []
        for _ in range(len(stack)):
            r = stack.pop(0)
            tmp.append(r.val)
            if r.left:
                stack.append(r.left)
            if r.right:
                stack.append(r.right)
        res.append(tmp)
    return res
print(levelOrder(l1_1))


def postorderTraversal(root):
    res = []
    stack = [root,]
    while stack and root:
        root = stack.pop()
        res.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return res[::-1]
print(postorderTraversal(l1_1))
