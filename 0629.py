class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_4 = ListNode(6)
l1_5 = ListNode(8)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = None

def hasCycle(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
print(hasCycle(l1_1))

# def detectCycle(head):
#     fast = slow = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if fast == slow:
#             break
#     slow = head
#     while slow != fast:
#         slow = slow.next
#         fast = fast.next
#     return slow
# print(detectCycle(l1_1))

def binarySearch(nums,target):
    left = 0
    right = len(nums)
    while left < right:
        mid = int(left + (right - left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
nums = [1,2,3,5,6]
target = 1
print(binarySearch(nums,target))

def findBinary(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val
print(findBinary(l1_1))

def lastK(head,K):
    slow = fast = head
    for i in range(K):
        fast = fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    return slow.val
print(lastK(l1_1,2))

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

