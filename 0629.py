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
