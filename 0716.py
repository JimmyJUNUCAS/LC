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

def isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.right,q.right) and isSameTree(p.left,q.left)
print(isSameTree(l1_1,l1_1))

from collections import deque
def isSameTree(p,q):
    def check(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True
    deq = deque([(p,q),])
    while deq:
        p,q = deq.popleft()
        if not check(p,q):
            return False
        if p:
            deq.append((p.left,q.left))
            deq.append((p.right,q.right))
    return True
print(isSameTree(l1_1,l1_1))

def isSymmetric(root):
    if not root:
        return True
    def dfs(left,right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return dfs(left.left,right.right) and dfs(left.right,right.left)
    return dfs(root.left,root.right)
print(isSymmetric(l1_1))

def isSymmetric(root):
    if not root or not (root.left or root.right):
        return True
    queue = [root.left,root.right]
    while queue:
        left = queue.pop(0)
        right = queue.pop(0)
        if not (left or right):
            continue
        if not (left and right):
            return False
        if left.val != right.val:
            queue.append(left.right)
            queue.append(right.left)
    return True
print(isSymmetric(l1_1))

def sortedArrayToBST(nums):
    def helper(left,right):
        if left > right:
            return None
        p = (left+right)//2
        root = TreeNode(nums[p])
        root.left = helper(left,p-1)
        root.right = helper(p+1,right)
        return root
    return helper(0,len(nums)-1)

def sortedArrayToBST(nums):
    def helper(left,right):
        if left > right:
            return None
        p = (left+right)//2
        if (left+right) % 2:
            p += 1
        root = TreeNode(nums[p])
        root.left = helper(left,p-1)
        root.right = helper(p+1,right)
        return root
    return helper(0,len(nums)-1)

from random import randint
def sortedArrayToBST(nums):
    def helper(left,right):
        if left > right:
            return None
        p = (left+right)//2
        if (left+right) % 2:
            p += randint(0,1)
        root = TreeNode(nums[p])
        root.left = helper(left,p-1)
        root.right = helper(p+1,right)
        return root
    return helper(0,len(nums)-1)
nums = [-10,-3,0,5,9]
print(sortedArrayToBST(nums))